const itemsInput = document.getElementById("items");
const capacityInput = document.getElementById("capacity");
const optimizeBtn = document.getElementById("optimizeBtn");
const sampleBtn = document.getElementById("sampleBtn");
const results = document.getElementById("results");
const errorBox = document.getElementById("error");
const algorithmSelect = document.getElementById("algorithmSelect");

let latestResults = null;


sampleBtn.addEventListener("click", () => {
    itemsInput.value =
        "0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5";

    capacityInput.value = "1.0";
});


optimizeBtn.addEventListener("click", async () => {
    errorBox.textContent = "";

    const items = itemsInput.value
        .split(",")
        .map(x => Number(x.trim()))
        .filter(x => !Number.isNaN(x));

    const capacity = Number(capacityInput.value);

    if (!items.length || !capacity) {
        errorBox.textContent = "Please enter valid values.";
        return;
    }

    try {
        optimizeBtn.disabled = true;
        optimizeBtn.textContent = "Optimizing...";

        const response = await fetch("/optimize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                items,
                capacity
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error);
        }

        latestResults = data;

        showResults(data);

    } catch (error) {
        errorBox.textContent = error.message;
    } finally {
        optimizeBtn.disabled = false;
        optimizeBtn.textContent = "Optimize Packing →";
    }
});


function showResults(data) {
    results.classList.remove("hidden");

    document.getElementById("lowerBound").textContent =
        data.lower_bound;

    document.getElementById("totalWeight").textContent =
        data.total.toFixed(1);

    const algorithms = data.algorithms;

    const best = Math.min(
        algorithms.FF.bins_used,
        algorithms.FFD.bins_used,
        algorithms.BFD.bins_used
    );

    document.getElementById("bestResult").textContent =
        `${best} bins`;

    const comparison = document.getElementById("comparison");

    comparison.innerHTML = "";

    Object.entries(algorithms).forEach(([key, algorithm]) => {

        const efficiency =
            (data.lower_bound / algorithm.bins_used) * 100;

        const row = document.createElement("div");
        row.className = "comparison-row";

        row.innerHTML = `
            <strong class="${algorithm.bins_used === best ? "best" : ""}">
                ${algorithm.name}
            </strong>

            <span>
                ${algorithm.bins_used} bins
            </span>

            <span>
                ${efficiency.toFixed(1)}% efficiency
            </span>
        `;

        comparison.appendChild(row);
    });

    renderBins();
}


algorithmSelect.addEventListener("change", renderBins);


function renderBins() {
    if (!latestResults) return;

    const selected = algorithmSelect.value;
    const bins = latestResults.algorithms[selected].bins;
    const container = document.getElementById("bins");

    container.innerHTML = "";

    bins.forEach(bin => {

        const binElement = document.createElement("div");
        binElement.className = "bin";

        const header = document.createElement("div");
        header.className = "bin-header";

        header.innerHTML = `
            <span>Bin ${bin.number}</span>
            <span>
                ${bin.used.toFixed(1)} / ${latestResults.capacity}
                (${bin.utilization}%)
            </span>
        `;

        const bar = document.createElement("div");
        bar.className = "bar";

        bin.items.forEach(item => {
            const itemElement = document.createElement("div");

            itemElement.className = "item";
            itemElement.style.width =
                `${(item / latestResults.capacity) * 100}%`;

            itemElement.textContent = item;

            bar.appendChild(itemElement);
        });

        const itemList = document.createElement("div");
        itemList.className = "item-list";

        itemList.textContent =
            `Items: ${bin.items.join(", ")}`;

        binElement.appendChild(header);
        binElement.appendChild(bar);
        binElement.appendChild(itemList);

        container.appendChild(binElement);
    });
}


window.addEventListener("load", () => {
    optimizeBtn.click();
});
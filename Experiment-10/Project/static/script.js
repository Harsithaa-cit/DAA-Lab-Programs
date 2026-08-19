const compareBtn = document.getElementById("compareBtn");
const singleBtn = document.getElementById("singleBtn");

const inputType = document.getElementById("inputType");
const arraySize = document.getElementById("arraySize");

const loading = document.getElementById("loading");
const errorBox = document.getElementById("error");
const results = document.getElementById("results");


function showLoading() {

    loading.classList.remove("hidden");
    errorBox.classList.add("hidden");

    compareBtn.disabled = true;
    singleBtn.disabled = true;
}


function hideLoading() {

    loading.classList.add("hidden");

    compareBtn.disabled = false;
    singleBtn.disabled = false;
}


function showError(message) {

    errorBox.textContent = message;

    errorBox.classList.remove("hidden");

    results.classList.add("hidden");
}


function formatNumber(number) {

    return Number(number).toLocaleString();
}


function displayComparison(data) {

    results.classList.remove("hidden");

    document.getElementById("resultSize").textContent =
        formatNumber(data.size);

    document.getElementById("inputBadge").textContent =
        data.input_type.replace("_", " ").toUpperCase();


    // Comparison values

    const dComparisons =
        data.deterministic.comparisons;

    const rComparisons =
        data.randomized.comparisons;


    document.getElementById("dComparisons").textContent =
        formatNumber(dComparisons);

    document.getElementById("rComparisons").textContent =
        formatNumber(rComparisons);


    document.getElementById("dCompDetail").textContent =
        formatNumber(dComparisons);

    document.getElementById("rCompDetail").textContent =
        formatNumber(rComparisons);


    // Time

    document.getElementById("dTime").textContent =
        data.deterministic.time.toFixed(4);

    document.getElementById("rTime").textContent =
        data.randomized.time.toFixed(4);


    // Winner

    const dTime = data.deterministic.time;
    const rTime = data.randomized.time;

    let winner;

    if (dTime < rTime) {

        winner = "Deterministic";

    } else {

        winner = "Randomized";

    }

    document.getElementById("winner").textContent =
        winner;


    // Bars

    const maxComparisons =
        Math.max(
            dComparisons,
            rComparisons,
            1
        );

    document.getElementById("dBar").style.width =
        `${(dComparisons / maxComparisons) * 100}%`;

    document.getElementById("rBar").style.width =
        `${(rComparisons / maxComparisons) * 100}%`;


    document.getElementById("dBarValue").textContent =
        formatNumber(dComparisons);

    document.getElementById("rBarValue").textContent =
        formatNumber(rComparisons);


    // Explanation

    const input = data.input_type;

    let explanation = "";

    if (
        input === "sorted" ||
        input === "reverse"
    ) {

        explanation =
            "For this input, Deterministic Quick Sort " +
            "uses the last element as the pivot. " +
            "Because the input is already ordered, " +
            "the pivot becomes the smallest or largest " +
            "element repeatedly, causing O(n²) behavior. " +
            "Randomized Quick Sort avoids this predictable " +
            "behavior by selecting the pivot randomly.";

    } else if (
        input === "nearly_sorted"
    ) {

        explanation =
            "Nearly sorted input can still cause " +
            "Deterministic Quick Sort to perform poorly " +
            "because its fixed pivot strategy is sensitive " +
            "to input ordering. Randomized pivot selection " +
            "provides more robust expected O(n log n) performance.";

    } else {

        explanation =
            "For random input, both algorithms generally " +
            "perform close to O(n log n). Randomized Quick Sort " +
            "provides protection against unfavorable input " +
            "orders by selecting the pivot randomly.";

    }

    document.getElementById("explanationText").textContent =
        explanation;
}


// --------------------------------------------------
// Compare Button
// --------------------------------------------------

compareBtn.addEventListener("click", async () => {

    showLoading();

    try {

        const response = await fetch(
            "/compare",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    input_type:
                        inputType.value,

                    size:
                        Number(arraySize.value)

                })

            }
        );


        const data = await response.json();


        if (!response.ok || !data.success) {

            throw new Error(
                data.error ||
                "Unable to run comparison."
            );

        }


        displayComparison(data);

    } catch (error) {

        showError(error.message);

    } finally {

        hideLoading();

    }

});


// --------------------------------------------------
// Single Algorithm Button
// --------------------------------------------------

singleBtn.addEventListener("click", async () => {

    showLoading();

    try {

        const algorithm =
            confirm(
                "Click OK for Randomized Quick Sort.\n" +
                "Click Cancel for Deterministic Quick Sort."
            )
            ? "randomized"
            : "deterministic";


        const response = await fetch(
            "/sort",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    input_type:
                        inputType.value,

                    algorithm:
                        algorithm,

                    size:
                        Number(arraySize.value)

                })

            }
        );


        const data = await response.json();


        if (!response.ok || !data.success) {

            throw new Error(
                data.error ||
                "Unable to run algorithm."
            );

        }


        alert(
            `${data.algorithm}\n\n` +
            `Array Size: ${data.size}\n` +
            `Comparisons: ${formatNumber(data.comparisons)}\n` +
            `Execution Time: ${data.time} ms`
        );


    } catch (error) {

        showError(error.message);

    } finally {

        hideLoading();

    }

});
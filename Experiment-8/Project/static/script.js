const cityCount = document.getElementById("cityCount");
const matrixContainer = document.getElementById("matrixContainer");
const sampleBtn = document.getElementById("sampleBtn");
const solveBtn = document.getElementById("solveBtn");

const errorMessage = document.getElementById("errorMessage");
const emptyState = document.getElementById("emptyState");
const resultContent = document.getElementById("resultContent");
const status = document.getElementById("status");

const sampleMatrices = {

    4: [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ],

    5: [
        [0, 10, 8, 9, 7],
        [10, 0, 10, 5, 6],
        [8, 10, 0, 8, 9],
        [9, 5, 8, 0, 6],
        [7, 6, 9, 6, 0]
    ],

    6: [
        [0, 10, 15, 20, 18, 12],
        [10, 0, 12, 8, 14, 16],
        [15, 12, 0, 10, 9, 11],
        [20, 8, 10, 0, 7, 13],
        [18, 14, 9, 7, 0, 6],
        [12, 16, 11, 13, 6, 0]
    ]

};


function cityName(index) {

    return String.fromCharCode(65 + index);

}


function renderMatrix(values = null) {

    const n = Number(cityCount.value);

    const matrix = document.createElement("table");

    matrix.className = "matrix";


    const header = document.createElement("tr");

    header.appendChild(document.createElement("th"));


    for (let i = 0; i < n; i++) {

        const th = document.createElement("th");

        th.textContent = cityName(i);

        header.appendChild(th);

    }


    matrix.appendChild(header);


    for (let i = 0; i < n; i++) {

        const row = document.createElement("tr");

        const label = document.createElement("th");

        label.textContent = cityName(i);

        row.appendChild(label);


        for (let j = 0; j < n; j++) {

            const td = document.createElement("td");

            const input = document.createElement("input");

            input.type = "number";

            input.min = "0";

            input.step = "1";

            input.dataset.row = i;

            input.dataset.col = j;


            if (i === j) {

                input.value = 0;

                input.readOnly = true;

                input.classList.add("diagonal");

            }

            else if (values) {

                input.value = values[i][j];

            }


            td.appendChild(input);

            row.appendChild(td);

        }


        matrix.appendChild(row);

    }


    matrixContainer.replaceChildren(matrix);

}


function getMatrix() {

    const n = Number(cityCount.value);

    const inputs =
        [...document.querySelectorAll(".matrix input")];

    const matrix =
        Array.from(
            { length: n },
            () => Array(n).fill(0)
        );


    for (const input of inputs) {

        const i = Number(input.dataset.row);

        const j = Number(input.dataset.col);

        const value = input.value.trim();


        if (value === "") {

            throw new Error(
                `Enter a cost for ${cityName(i)} → ${cityName(j)}.`
            );

        }


        const number = Number(value);


        if (!Number.isFinite(number) || number < 0) {

            throw new Error(
                `Invalid cost at ${cityName(i)} → ${cityName(j)}.`
            );

        }


        matrix[i][j] = number;

    }


    return matrix;

}


function showError(message) {

    errorMessage.textContent = message;

}


function renderRoute(route) {

    const container =
        document.getElementById("routeDisplay");

    container.replaceChildren();


    route.forEach((city, index) => {

        const node = document.createElement("span");

        node.className = "city-node";

        node.textContent = city;

        container.appendChild(node);


        if (index < route.length - 1) {

            const arrow = document.createElement("span");

            arrow.className = "route-arrow";

            arrow.textContent = "→";

            container.appendChild(arrow);

        }

    });

}


function renderVerification(items) {

    const container =
        document.getElementById("verificationList");

    container.replaceChildren();


    items.forEach(item => {

        const row = document.createElement("div");

        row.className = "edge-row";


        const edge = document.createElement("span");

        edge.textContent =
            `${item.from} → ${item.to}`;


        const cost = document.createElement("span");

        cost.className = "edge-cost";

        cost.textContent = item.cost;


        row.append(edge, cost);

        container.appendChild(row);

    });

}


async function solve() {

    showError("");

    solveBtn.disabled = true;

    solveBtn.style.opacity = "0.65";

    status.textContent = "SOLVING…";


    try {

        const matrix = getMatrix();


        const response = await fetch(
            "/solve",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    matrix: matrix
                })
            }
        );


        const data = await response.json();


        if (!response.ok || !data.success) {

            throw new Error(
                data.error ||
                "Unable to solve the problem."
            );

        }


        document.getElementById(
            "minimumCost"
        ).textContent = data.cost;


        document.getElementById(
            "cityTotal"
        ).textContent = matrix.length;


        document.getElementById(
            "executionTime"
        ).textContent =
            `${data.time_ms} ms`;


        renderRoute(data.route);

        renderVerification(data.verification);


        emptyState.classList.add("hidden");

        resultContent.classList.remove("hidden");

        status.textContent = "SOLVED";

        status.classList.add("solved");

    }

    catch (error) {

        showError(error.message);

        status.textContent = "ERROR";

        status.classList.remove("solved");

    }

    finally {

        solveBtn.disabled = false;

        solveBtn.style.opacity = "1";

    }

}


cityCount.addEventListener(
    "change",
    () => {

        renderMatrix(
            sampleMatrices[
                Number(cityCount.value)
            ]
        );

        emptyState.classList.remove(
            "hidden"
        );

        resultContent.classList.add(
            "hidden"
        );

        status.textContent = "READY";

        status.classList.remove(
            "solved"
        );

        showError("");

    }
);


sampleBtn.addEventListener(
    "click",
    () => {

        renderMatrix(
            sampleMatrices[
                Number(cityCount.value)
            ]
        );

        showError("");

    }
);


solveBtn.addEventListener(
    "click",
    solve
);


renderMatrix(sampleMatrices[5]);
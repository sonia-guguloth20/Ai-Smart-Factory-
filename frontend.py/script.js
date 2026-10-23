async function loadFactoryStatus() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/status"
        );

        const data = await response.json();

        document.getElementById("factory-status").innerText =
            data.factory_status;

        document.getElementById("workers").innerText =
            data.workers;

        document.getElementById("ppe").innerText =
            data.ppe_compliant + " / " + data.workers;

        document.getElementById("violations").innerText =
            data.violations;

        document.getElementById("fire").innerText =
            data.fire_detected ? "DETECTED" : "NO";

    }

    catch (error) {

        console.error("Backend connection failed:", error);

    }
}


loadFactoryStatus();
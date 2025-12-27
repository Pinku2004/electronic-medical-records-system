function getStats() {
    const patientId = document.getElementById("patientId").value;

    fetch("/stats", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ patientId })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("output").innerText = data.result;
    });
}

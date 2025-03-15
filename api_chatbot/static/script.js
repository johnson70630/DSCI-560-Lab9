async function uploadPDFs() {
    let files = document.getElementById('pdfUpload').files;
    if (files.length === 0) {
        alert("Please select a PDF file to upload.");
        return;
    }

    let formData = new FormData();
    for (let file of files) {
        formData.append("files", file);
    }

    let response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    let result = await response.json();
    alert(result.message);
}

async function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    if (!userInput) return;

    let chatBox = document.getElementById("chatBox");
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

    let response = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userInput })
    });

    let data = await response.json();
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.answer}</p>`;

    document.getElementById("userInput").value = "";
}

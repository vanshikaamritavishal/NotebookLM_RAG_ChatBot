const BASE_URL = "http://127.0.0.1:10000";

function formatAnswer(text) {

    const lines = text.split("\n");

    let formatted = "";

    let inList = false;

    lines.forEach(line => {

        line = line.trim();

        if (!line) return;

        if (line.match(/^(\d+\.|-|\*)\s/)) {

            if (!inList) {
                formatted += "<ul>";
                inList = true;
            }

            line = line.replace(/^(\d+\.|-|\*)\s/, "");

            formatted += `<li>${line}</li>`;

        } else {

            if (inList) {
                formatted += "</ul>";
                inList = false;
            }

            formatted += `<p>${line}</p>`;
        }
    });

    if (inList) {
        formatted += "</ul>";
    }

    return formatted;
}

async function uploadFile() {

    const fileInput = document.getElementById("fileInput");

    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file.");
        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

        const response = await fetch(
            `${BASE_URL}/upload`,
            {
                method: "POST",
                body: formData
            }
        );

        if (!response.ok) {
            throw new Error("Upload failed");
        }

        const data = await response.json();

        alert("Document uploaded successfully!");

        console.log(data);

    } catch (error) {

        console.error(error);

        alert("Upload failed.");
    }
}

async function askQuestion() {

    const question = document.getElementById("question").value;

    const answerDiv = document.getElementById("answer");

    if (!question) {
        return;
    }

    answerDiv.innerHTML = "Thinking...";

    try {

        const response = await fetch(
            `${BASE_URL}/ask`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    question: question
                })
            }
        );

        if (!response.ok) {
            throw new Error("Request failed");
        }

        const data = await response.json();

        answerDiv.innerHTML = formatAnswer(data.answer);

    } catch (error) {

        console.error(error);

        answerDiv.innerHTML = "Error generating response.";
    }
}
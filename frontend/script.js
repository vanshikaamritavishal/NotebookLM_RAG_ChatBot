const YOUR_RENDER_BACKEND_URL = "https://notebooklm-rag-backend.onrender.com";
function formatAnswer(text) {

    const lines = text.split("\n");

    let formatted = "";

    let inList = false;

    lines.forEach(line => {

        line = line.trim();

        if (
            line.match(/^(\d+\.|-|\*)\s/)
        ) {

            if (!inList) {
                formatted += "<ul>";
                inList = true;
            }

            line = line.replace(/^(\d+\.|-|\*)\s/, "");

            formatted += `<li>${line.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")}</li>`;

        } else {

            if (inList) {
                formatted += "</ul>";
                inList = false;
            }

            if (line !== "") {
                formatted += `<p>${line.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")}</p>`;
            }
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
            `${YOUR_RENDER_BACKEND_URL}/upload`,
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        alert("Document uploaded successfully!");

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
            `${YOUR_RENDER_BACKEND_URL}/ask`,
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

        const data = await response.json();

        answerDiv.innerHTML = formatAnswer(data.answer);

    } catch (error) {

        console.error(error);

        answerDiv.innerHTML = "Error generating response.";
    }
}

const questionInput = document.getElementById("question");

questionInput.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        askQuestion();
    }
});

const fileInput = document.getElementById("fileInput");

const uploadBtn = document.getElementById("uploadBtn");

fileInput.addEventListener("change", function() {

    if (fileInput.files.length > 0) {

        uploadBtn.disabled = false;

        uploadBtn.classList.add("active-upload");

    } else {

        uploadBtn.disabled = true;

        uploadBtn.classList.remove("active-upload");
    }
});
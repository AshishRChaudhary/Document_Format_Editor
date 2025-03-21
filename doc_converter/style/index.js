document.getElementById("fileInput").addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (file) {
        document.getElementById("uploadBox").classList.add("hidden");
        document.getElementById("fileName").textContent = file.name;
        document.getElementById("fileName").classList.remove("hidden");
        document.getElementById("convertBtn").disabled = false;
    }
});

document.getElementById("convertBtn").addEventListener("click", async function() {
    const fileInput = document.getElementById("fileInput").files[0];
    
    if (!fileInput) return;

    document.getElementById("loader").classList.remove("hidden");

    const formData = new FormData();
    formData.append("file", fileInput);

    try {
        const response = await fetch("http://127.0.0.1:8000/convert/", {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            const blob = await response.blob();
            const downloadUrl = URL.createObjectURL(blob);
            const downloadLink = document.getElementById("downloadLink");
            
            downloadLink.href = downloadUrl;
            downloadLink.download = "converted.pdf";
            downloadLink.classList.remove("hidden");
        }
    } catch (error) {
        console.error("Error:", error);
    } finally {
        document.getElementById("loader").classList.add("hidden");
    }
});

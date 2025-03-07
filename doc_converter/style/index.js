
    document.getElementById("fileInput").addEventListener("change", function(event) {
        const file = event.target.files[0];
        if (file) {
            document.getElementById("fileName").textContent = "Selected: " + file.name;
            document.getElementById("convertBtn").disabled = false;
        }
    });

    document.getElementById("convertBtn").addEventListener("click", function() {
        document.getElementById("loader").classList.remove("hidden");
        setTimeout(() => {
            document.getElementById("loader").classList.add("hidden");
            document.getElementById("downloadLink").classList.remove("hidden");
            document.getElementById("downloadLink").setAttribute("href", "#");
        }, 2000);
    });

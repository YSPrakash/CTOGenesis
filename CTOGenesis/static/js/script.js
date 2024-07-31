document.addEventListener("DOMContentLoaded", function () {
  const uploadButton = document.getElementById("mfu-new-item-btn");
  const fileInput = document.getElementById("mfu-file-1");

  // Check if the upload button and file input elements exist
  if (!uploadButton || !fileInput) {
    console.error("Upload button or file input element not found.");
    return;
  }

  uploadButton.addEventListener("click", function () {
    const formData = new FormData();

    // Check if files are selected
    if (fileInput.files.length === 0) {
      alert("Please select a file first.");
      return;
    }

    formData.append("file", fileInput.files[0]);

    fetch("/upload", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          return response.blob(); // Process the response as a Blob
        } else {
          return response.json().then((data) => Promise.reject(data));
        }
      })
      .then((blob) => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "response.py"; // Name of the file to download
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred while processing the file.");
      });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const uploadButton2 = document.getElementById("mfu-new-item-btn2");
  const fileInput2 = document.getElementById("mfu-file-1");

  // Check if the upload button and file input elements exist
  if (!uploadButton2 || !fileInput2) {
    console.error("Upload button or file input element not found.");
    return;
  }

  uploadButton2.addEventListener("click", function () {
    const formData = new FormData();

    // Check if files are selected
    if (fileInput2.files.length === 0) {
      alert("Please select a file first.");
      return;
    }

    formData.append("file", fileInput2.files[0]);

    fetch("/upload2", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          return response.blob(); // Process the response as a Blob
        } else {
          return response.json().then((data) => Promise.reject(data));
        }
      })
      .then((blob) => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "response2.txt"; // Name of the file to download
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred while processing the file.");
      });
  });
});

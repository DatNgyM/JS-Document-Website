document.getElementById("search-bar").addEventListener("keyup", function () {
    let filter = this.value.toLowerCase();
    let sections = document.querySelectorAll(".main-section");

    sections.forEach(section => {
        let text = section.innerText.toLowerCase();
        if (text.includes(filter)) {
            section.style.display = "block";
        } else {
            section.style.display = "none";
        }
    });
});

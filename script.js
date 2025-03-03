document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-bar");
    const sections = document.querySelectorAll(".main-section");

    searchInput.addEventListener("keyup", function () {
        let searchText = searchInput.value.trim().toLowerCase();
        let regex = new RegExp(`\\b(${searchText})\\b`, "gi"); // Chỉ tìm kiếm từ hoàn chỉnh

        sections.forEach(section => {
            // Lấy nội dung gốc trước khi tô màu
            let originalText = section.getAttribute("data-original-text");
            if (!originalText) {
                section.setAttribute("data-original-text", section.innerHTML);
                originalText = section.innerHTML;
            }

            if (searchText.length > 0) {
                let highlightedText = originalText.replace(regex, `<span class="highlight">$1</span>`);
                section.innerHTML = highlightedText;
            } else {
                // Nếu ô tìm kiếm rỗng, trả lại nội dung gốc
                section.innerHTML = originalText;
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const menu = document.getElementById("menuPrincipal");
    document.querySelectorAll("#menuPrincipal .nav-link").forEach((link) => {
        link.addEventListener("click", () => {
            if (menu.classList.contains("show")) {
                bootstrap.Collapse.getOrCreateInstance(menu).hide();
            }
        });
    });
});
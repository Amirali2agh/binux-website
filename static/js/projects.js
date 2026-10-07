(() => {
    const modal = document.getElementById("project-modal");
    const dataEl = document.getElementById("portfolio-projects-data");
    if (!modal || !dataEl) return;

    const projects = JSON.parse(dataEl.textContent || "[]");
    let activeProject = null;
    let activeIndex = 0;

    const titleEl = document.getElementById("project-modal-title");
    const categoryEl = document.getElementById("project-modal-category");
    const summaryEl = document.getElementById("project-modal-summary");
    const descriptionEl = document.getElementById("project-modal-description");
    const techEl = document.getElementById("project-modal-tech");
    const imageEl = document.getElementById("project-modal-image");
    const emptyEl = document.getElementById("project-modal-empty");
    const captionEl = document.getElementById("project-modal-caption");
    const thumbsEl = document.getElementById("project-modal-thumbs");
    const prevEl = document.getElementById("project-prev");
    const nextEl = document.getElementById("project-next");
    const linkEl = document.getElementById("project-modal-link");

    function activeImages() {
        if (!activeProject) return [];
        if (activeProject.images.length) return activeProject.images;
        return activeProject.cover_image ? [{ url: activeProject.cover_image, alt: activeProject.title, caption: "" }] : [];
    }

    function renderAlbum() {
        const images = activeImages();
        thumbsEl.innerHTML = "";

        if (!images.length) {
            imageEl.classList.add("hidden");
            emptyEl.classList.remove("hidden");
            emptyEl.classList.add("flex");
            prevEl.classList.add("hidden");
            nextEl.classList.add("hidden");
            captionEl.textContent = "";
            return;
        }

        imageEl.classList.remove("hidden");
        emptyEl.classList.add("hidden");
        emptyEl.classList.remove("flex");
        activeIndex = Math.min(activeIndex, images.length - 1);

        const current = images[activeIndex];
        imageEl.src = current.url;
        imageEl.alt = current.alt || activeProject.title;
        captionEl.textContent = current.caption || "";

        if (images.length > 1) {
            prevEl.classList.remove("hidden");
            nextEl.classList.remove("hidden");
        } else {
            prevEl.classList.add("hidden");
            nextEl.classList.add("hidden");
        }

        images.forEach((item, index) => {
            const thumb = document.createElement("button");
            thumb.type = "button";
            thumb.className = "shrink-0 w-20 h-14 rounded-lg overflow-hidden border transition-all " + (index === activeIndex ? "border-brand-accent" : "border-slate-800 opacity-60 hover:opacity-100");
            thumb.setAttribute("aria-label", "تصویر " + (index + 1));
            const img = document.createElement("img");
            img.src = item.url;
            img.alt = item.alt || activeProject.title;
            img.className = "w-full h-full object-cover";
            thumb.appendChild(img);
            thumb.addEventListener("click", () => {
                activeIndex = index;
                renderAlbum();
            });
            thumbsEl.appendChild(thumb);
        });
    }

    function renderProject() {
        titleEl.textContent = activeProject.title;
        categoryEl.textContent = activeProject.category;
        summaryEl.textContent = activeProject.short_description;
        descriptionEl.textContent = activeProject.description;
        techEl.innerHTML = "";

        activeProject.technologies.forEach((tech) => {
            const tag = document.createElement("span");
            tag.className = "px-2.5 py-1 rounded-md border border-slate-800 bg-brand-dark text-[10px] font-mono text-slate-400";
            tag.textContent = tech;
            techEl.appendChild(tag);
        });

        if (activeProject.project_url) {
            linkEl.href = activeProject.project_url;
            linkEl.textContent = activeProject.project_url_label || "مشاهده پروژه";
            linkEl.classList.remove("hidden");
        } else {
            linkEl.classList.add("hidden");
            linkEl.removeAttribute("href");
        }

        activeIndex = 0;
        renderAlbum();
    }

    window.openProjectModal = function(slug) {
        activeProject = projects.find((project) => project.slug === slug);
        if (!activeProject) return;
        renderProject();
        modal.classList.remove("hidden");
        modal.classList.add("flex");
        modal.setAttribute("aria-hidden", "false");
        document.body.classList.add("overflow-hidden");
    };

    window.closeProjectModal = function() {
        modal.classList.add("hidden");
        modal.classList.remove("flex");
        modal.setAttribute("aria-hidden", "true");
        document.body.classList.remove("overflow-hidden");
        activeProject = null;
    };

    prevEl.addEventListener("click", () => {
        const images = activeImages();
        if (!images.length) return;
        activeIndex = (activeIndex - 1 + images.length) % images.length;
        renderAlbum();
    });

    nextEl.addEventListener("click", () => {
        const images = activeImages();
        if (!images.length) return;
        activeIndex = (activeIndex + 1) % images.length;
        renderAlbum();
    });

    modal.addEventListener("click", (event) => {
        if (event.target === modal) window.closeProjectModal();
    });

    document.addEventListener("keydown", (event) => {
        if (modal.classList.contains("hidden")) return;
        if (event.key === "Escape") window.closeProjectModal();
        if (event.key === "ArrowLeft") prevEl.click();
        if (event.key === "ArrowRight") nextEl.click();
    });

    document.querySelectorAll("[data-project-slug]").forEach((card) => {
        card.addEventListener("keydown", (event) => {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                window.openProjectModal(card.dataset.projectSlug);
            }
        });
    });
})();
document.addEventListener("DOMContentLoaded", () => {
  const CONFIG = {
    flatpakDownloadUrl: "https://github.com/vitordevsp/todolist-gtk/releases/download/v0.1.1/todolist.flatpak",
    leadFormEndpoint: "https://studio-functions.vercel.app/api/leads",
  };

  if (window.lucide) {
    window.lucide.createIcons();
  }

  const mobileMenuButton = document.querySelector("#mobile-menu-button");
  const mobileMenu = document.querySelector("#mobile-menu");
  const mobileLinks = mobileMenu ? mobileMenu.querySelectorAll("a[href^='#']") : [];
  const siteHeader = document.querySelector("#site-header");
  const githubCorner = document.querySelector("#github-corner");
  const form = document.querySelector("#lead-form");
  const nameInput = document.querySelector("#lead-name");
  const emailInput = document.querySelector("#lead-email");
  const messageInput = document.querySelector("#lead-message");
  const feedback = document.querySelector("#lead-feedback");
  const revealItems = document.querySelectorAll("[data-reveal]");
  const currentYear = document.querySelector("#current-year");
  const imageTriggers = document.querySelectorAll("[data-lightbox-trigger]");
  const imageLightbox = document.querySelector("#image-lightbox");
  const imageLightboxClose = document.querySelector("#image-lightbox-close");
  const imageLightboxContent = document.querySelector("#image-lightbox-content");
  const toast = document.querySelector("#toast");
  const flatpakDownloadLink = document.querySelector("[data-flatpak-download]");
  let toastTimer;
  let toastExitTimer;
  let lastScrollY = window.scrollY;
  let ticking = false;

  if (currentYear) {
    currentYear.textContent = String(new Date().getFullYear());
  }

  if (flatpakDownloadLink && CONFIG.flatpakDownloadUrl) {
    flatpakDownloadLink.setAttribute("href", CONFIG.flatpakDownloadUrl);
    flatpakDownloadLink.setAttribute("target", "_blank");
    flatpakDownloadLink.setAttribute("rel", "noreferrer");
  }

  if (siteHeader) {
    const showHeader = () => {
      siteHeader.classList.remove("is-hidden");
      githubCorner?.classList.add("pointer-events-none", "opacity-0");
      githubCorner?.classList.remove("pointer-events-auto", "opacity-100");
    };

    const hideHeader = () => {
      siteHeader.classList.add("is-hidden");
      githubCorner?.classList.remove("pointer-events-none", "opacity-0");
      githubCorner?.classList.add("pointer-events-auto", "opacity-100");
    };

    const updateHeaderVisibility = () => {
      const currentScrollY = window.scrollY;
      const isMenuOpen = mobileMenu ? !mobileMenu.classList.contains("hidden") : false;
      const scrollDelta = currentScrollY - lastScrollY;

      if (Math.abs(scrollDelta) < 4) {
        ticking = false;
        return;
      }

      if (currentScrollY < 80 || isMenuOpen || scrollDelta < 0) {
        showHeader();
      } else if (currentScrollY > 140) {
        hideHeader();
      }

      lastScrollY = currentScrollY;
      ticking = false;
    };

    window.addEventListener(
      "scroll",
      () => {
        if (!ticking) {
          window.requestAnimationFrame(updateHeaderVisibility);
          ticking = true;
        }
      },
      { passive: true },
    );
  }

  if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener("click", () => {
      const isHidden = mobileMenu.classList.contains("hidden");
      mobileMenu.classList.toggle("hidden");
      mobileMenuButton.setAttribute("aria-expanded", String(isHidden));
      siteHeader?.classList.remove("is-hidden");
      githubCorner?.classList.add("pointer-events-none", "opacity-0");
      githubCorner?.classList.remove("pointer-events-auto", "opacity-100");
    });

    mobileLinks.forEach((link) => {
      link.addEventListener("click", () => {
        mobileMenu.classList.add("hidden");
        mobileMenuButton.setAttribute("aria-expanded", "false");
      });
    });
  }

  if ("IntersectionObserver" in window && revealItems.length > 0) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.12,
        rootMargin: "0px 0px -40px 0px",
      }
    );

    revealItems.forEach((item, index) => {
      item.style.transitionDelay = `${Math.min(index * 45, 220)}ms`;
      observer.observe(item);
    });
  } else {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  }

  if (imageTriggers.length > 0 && imageLightbox && imageLightboxClose && imageLightboxContent) {
    const openLightbox = (trigger) => {
      const src = trigger.getAttribute("data-lightbox-src");
      const alt = trigger.getAttribute("data-lightbox-alt");

      if (src) {
        imageLightboxContent.setAttribute("src", src);
      }

      if (alt) {
        imageLightboxContent.setAttribute("alt", alt);
      }

      imageLightbox.classList.remove("hidden");
      imageLightbox.classList.add("flex");
      imageLightbox.setAttribute("aria-hidden", "false");
      document.body.classList.add("overflow-hidden");
    };

    const closeLightbox = () => {
      imageLightbox.classList.add("hidden");
      imageLightbox.classList.remove("flex");
      imageLightbox.setAttribute("aria-hidden", "true");
      document.body.classList.remove("overflow-hidden");
    };

    imageTriggers.forEach((trigger) => {
      trigger.addEventListener("click", () => openLightbox(trigger));
    });
    imageLightboxClose.addEventListener("click", closeLightbox);
    imageLightbox.addEventListener("click", (event) => {
      if (event.target === imageLightbox) {
        closeLightbox();
      }
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !imageLightbox.classList.contains("hidden")) {
        closeLightbox();
      }
    });
  }

  if (!form || !nameInput || !emailInput || !messageInput || !feedback) {
    return;
  }

  const storageKey = "todolist-gtk-leads";
  const showToast = (message, type = "success") => {
    feedback.textContent = message;

    if (!toast) {
      return;
    }

    window.clearTimeout(toastTimer);
    window.clearTimeout(toastExitTimer);
    toast.innerHTML = [
      "<span class=\"flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-emerald-400/15 text-emerald-300\">",
      type === "error" ? "!" : "✓",
      "</span>",
      "<span class=\"leading-6\">",
      message,
      "</span>",
    ].join("");
    toast.className = [
      "pointer-events-none fixed right-5 top-5 z-50 flex max-w-sm translate-y-0 items-start gap-3 rounded-2xl px-5 py-4 text-sm font-medium opacity-100 shadow-card transition duration-300 ease-out",
      type === "error"
        ? "bg-amber-400 text-slate-950"
        : "bg-emerald-950/95 text-emerald-50 ring-1 ring-emerald-300/25",
    ].join(" ");

    toastTimer = window.setTimeout(() => {
      toast.classList.remove("translate-y-0", "opacity-100");
      toast.classList.add("-translate-y-3", "opacity-0");

      toastExitTimer = window.setTimeout(() => {
        toast.classList.add("hidden");
      }, 320);
    }, 3800);
  };

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = nameInput.value.trim();
    const email = emailInput.value.trim();
    const message = messageInput.value.trim();

    if (!name || !email) {
      showToast("Preencha nome e e-mail para entrar na lista.", "error");
      return;
    }

    if (!email.includes("@") || !email.includes(".")) {
      showToast("Digite um e-mail válido para entrar na lista.", "error");
      return;
    }

    const payload = {
      name,
      email,
      message,
      source: "todolist-gtk-landing",
      createdAt: new Date().toISOString(),
    };

    if (CONFIG.leadFormEndpoint) {
      try {
        const response = await fetch(CONFIG.leadFormEndpoint, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        });

        if (!response.ok) {
          throw new Error(`Lead request failed with status ${response.status}`);
        }

        showToast("Contato enviado. Vou te avisar quando houver algo concreto.");
        form.reset();
        return;
      } catch (error) {
        console.error(error);
        showToast("Não consegui enviar agora. Tenta de novo em alguns minutos.", "error");
        return;
      }
    }

    const currentLeads = JSON.parse(localStorage.getItem(storageKey) || "[]");
    const alreadyExists = currentLeads.some((entry) => entry.email === email);

    if (!alreadyExists) {
      currentLeads.push(payload);
      localStorage.setItem(storageKey, JSON.stringify(currentLeads));
    }

    showToast(
      alreadyExists
        ? "Esse e-mail já foi salvo aqui neste navegador."
        : "Contato salvo. Vou te avisar quando houver algo concreto.",
    );
    form.reset();
  });
});

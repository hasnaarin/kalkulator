if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
} else {
    document.documentElement.classList.remove('dark');
}

window.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');
    const sceneLight = document.getElementById('theme-scene-light');
    const sceneDark = document.getElementById('theme-scene-dark');

    const updateUI = (isDark) => {
        if (isDark) {
            if (themeToggleLightIcon) themeToggleLightIcon.classList.remove('hidden');
            if (themeToggleDarkIcon) themeToggleDarkIcon.classList.add('hidden');
            if (sceneLight) sceneLight.classList.add('hidden');
            if (sceneDark) sceneDark.classList.remove('hidden');
        } else {
            if (themeToggleLightIcon) themeToggleLightIcon.classList.add('hidden');
            if (themeToggleDarkIcon) themeToggleDarkIcon.classList.remove('hidden');
            if (sceneLight) sceneLight.classList.remove('hidden');
            if (sceneDark) sceneDark.classList.add('hidden');
        }
    };

    const isCurrentlyDark = localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches);
    updateUI(isCurrentlyDark);

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.theme = 'light';
                updateUI(false);
            } else {
                document.documentElement.classList.add('dark');
                localStorage.theme = 'dark';
                updateUI(true);
            }
        });
    }
});


setTimeout(() => location.reload(), 5 * 60 * 1000);
/*
function get_theme() {
  let theme = "light";
  if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
    theme = "dark";
  }
  console.debug("get_theme: ", theme);
  return theme;
}
window
  .matchMedia("(prefers-color-scheme: dark)")
  .addEventListener("change", set_theme);
function set_theme() {
  document.cookie = `theme=default-${get_theme()}`;
  const theme_style: HTMLStyleElement = document.querySelector(
    "#theme-style"
  ) as HTMLStyleElement;
  fetch(`http://localhost:8080/api/set-theme/default-${get_theme()}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  })
    .then((response) => response.text())
    .then((data) => {
      theme_style.innerHTML = data;
    });

  console.debug("set_theme: done");
}
set_theme();
*/
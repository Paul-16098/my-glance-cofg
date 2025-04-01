switch (pageData.slug) {
  case "Home":
  case "stats": {
    setTimeout(() => location.reload(), 1 * 60 * 1000);
    break;
  }
}

// document.onchange = function () {};

function bangadd() {
  const newbang = document.createElement("div");
  newbang.classList.add("bangscontainer");
  newbang.innerHTML =
    '<input class="bang" type="text" name="bang"/><input class="engin" type="text" name="engin"/>';
  const bangs = document.getElementById("bangs");
  bangs.insertBefore(newbang, bangs.lastElementChild);
  return false;
}

function appendQueryParams(event) {
  event.preventDefault();
  const form = event.target;
  const url = new URL(form.action);
  const formData = new FormData(form);
  formData.forEach((value, key) => {
    url.searchParams.append(key, value);
  });
  window.open(url.toString(), "_blank");
}

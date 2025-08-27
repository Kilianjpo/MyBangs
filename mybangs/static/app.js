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

const browser = document.getElementById("browser");
browser.addEventListener("change", (event) => {
  if (event.currentTarget.checked) {
    if (window.location.href.includes("?")) {
      document.getElementById("tut").innerHTML =
        '<p>Make sure you submited the form above.</p><p>Go to you browsers search settings.</p><p>Add the folowing url as search engin.</p><input class="engin" type="text" value="' +
        window.location.href +
      "&q=%s" +
        '" /><p>Start searching 💯 with your Bangs by typing your query followed by the Bang.<br />For example, "MyBangs !gh" to search this project on GitHub.</p>';
    } else {
      document.getElementById("tut").innerHTML =
        '<p>Make sure you submited the form above.</p><p>Go to you browsers search settings.</p><p>Add the folowing url as search engin.</p><input class="engin" type="text" value="' +
        window.location.href +
        "?q=%s" +
        '" /><p>Start searching 💯 with your Bangs by typing your query followed by the Bang.<br />For example, "MyBangs !gh" to search this project on GitHub.</p>';
    }
  } else {
    document.getElementById("tut").innerHTML =
      '<p>Make sure you submited the form above.</p><p>Right-click the browsers URL bar and then click on "Add MyBangs".</p><p>Set MyBangs as the default search engine in your browsers settings.</p><p>Start searching 💯 with your Bangs by typing your query followed by the Bang.<br />For example, "MyBangs !gh" to search this project on GitHub.</p>';
  }
});

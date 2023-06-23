var formFile = document.getElementById("formFile");
var previewFile = document.getElementById("previewFile");
formFile.addEventListener("change", function (event) {
  if (event.target.files.length == 0) {
    return;
  }
  var temporary_URL = URL.createObjectURL(event.target.files[0]);
  previewFile.setAttribute("src", temporary_URL);
  previewFile.setAttribute("width", "400px");
  previewFile.setAttribute("height", "250px");
  previewFile.setAttribute(
    "style",
    "border-style:solid; border-color:rgb(146, 106, 75); border-width:5px"
  );
});

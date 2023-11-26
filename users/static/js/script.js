function myFunction() {
	var x = document.getElementById("floatingPassword");
	if (x.type === "password") {
	  x.type = "text";
	} else {
	  x.type = "password";
	}
  }

  var element = document.getElementById("id_password1");
  element.classList.add("form-control");
  var element2 = document.getElementById("id_password2");
  element2.classList.add("form-control");

  const dropContainer = document.getElementById("dropcontainer")
  const fileInput = document.getElementById("images")

  dropContainer.addEventListener("dragover", (e) => {
    // prevent default to allow drop
    e.preventDefault()
  }, false)

  dropContainer.addEventListener("dragenter", () => {
    dropContainer.classList.add("drag-active")
  })

  dropContainer.addEventListener("dragleave", () => {
    dropContainer.classList.remove("drag-active")
  })

  dropContainer.addEventListener("drop", (e) => {
    e.preventDefault()
    dropContainer.classList.remove("drag-active")
    fileInput.files = e.dataTransfer.files
  })
 function addClass(link) {
  var links = document.getElementsByTagName("a");
  for(var i = 0; i < links.length; i++){
    links[i].classList.remove("active");
  }
  link.classList.add("active");
}
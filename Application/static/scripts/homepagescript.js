document.addEventListener('DOMContentLoaded', function() {
  var startButton = document.querySelector('.start-button');
  var optionsContainer = document.querySelector('.start_options');

  startButton.addEventListener('click', toggleOptions);

  function toggleOptions() {
    optionsContainer.classList.toggle('show-options');
  }
});

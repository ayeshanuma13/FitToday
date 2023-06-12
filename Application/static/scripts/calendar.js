function displayCalendar(completionData) {
    var calendar = document.getElementById("calendar");
    completionData.forEach(function(completion) {
      var completionDate = new Date(completion.completion_date);
      var completionDay = completionDate.getDate();
  
      // Find the day element in the calendar and mark it as completed
      var dayElement = calendar.querySelector('.day[data-day="' + completionDay + '"]');
      if (dayElement) {
        dayElement.classList.add("completed");
      }
    });
  }
  
const API_URL = "http://localhost:5000/events";

// Add one event to the page as a list item
function renderEvent(event) {
  const li = document.createElement("li");
  li.textContent = event.title;
  document.querySelector("#event-list").appendChild(li);
}

// Load existing events from the back end when the page opens
fetch(API_URL)
  .then(response => response.json())
  .then(events => {
    events.forEach(renderEvent);
  })
  .catch(error => console.error("Could not load events:", error));

// Send a new event to the back end when the form is submitted
document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();
  const titleInput = document.querySelector("#title");
  const title = titleInput.value.trim();

  // Validate input before sending the request
  if (!title) {
    alert("Please enter an event title.");
    return;
  }

  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  })
    .then(response => response.json())
    .then(newEvent => {
      renderEvent(newEvent);
      titleInput.value = "";
    })
    .catch(error => console.error("Could not add event:", error));
});
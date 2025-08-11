const form = document.getElementById("addEvent");
const previewBox = document.getElementById("eventPreview");
const saveBtn = document.getElementById("saveBtn");

form.addEventListener("input", () => {
  const title = form.title?.value || "";
  const location = form.location?.value || "";
  const venue = form.venue?.value || "";
  const date = form.date?.value || "";
  const startTime = form.start_time?.value || "";
  const endTime = form.end_time?.value || "";
  const imageUrl = form.image?.value || "";
  const description = form.description?.value || "";
  const brief = form.brief?.value || "";

  console.log(imageUrl);
  previewBox.innerHTML = `
    <h5>${title}</h5>
    <div class="d-flex justify-content-between">
      <p class="text-muted">Location: ${location}</p>
      <p class="text-muted">Venue: ${venue}</p>
      <p class="text-muted">Date: ${date}</p>
      <p class="text-muted">Start Time${startTime}</p>
      <p class="text-muted">End Time${endTime}</p>
    </div>
    <div class="event_description">
      <p>${brief}</p>
    </div>
  `
})
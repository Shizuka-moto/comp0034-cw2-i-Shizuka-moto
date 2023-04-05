// Function to delete a note by its noteId
function deleteNote(noteId) {
  // Send a POST request to the server to delete the note
  fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({ noteId }),
  })
    .then((_res) => {
      // Redirect to the home page after the note is deleted
      window.location.href = '/';
    });
}
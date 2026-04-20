const quoteForm = document.getElementById('quote-form');
const message = document.getElementById('form-message');

quoteForm?.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(quoteForm);
  const name = formData.get('name');
  message.textContent = `Thanks${name ? `, ${name}` : ''}! We'll reach out within one business day.`;
  quoteForm.reset();
});

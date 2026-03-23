// Shared utility functions used across all pages

function parseSkills(str) {
  return str.split(',').map(s => s.trim()).filter(Boolean);
}

function showLoading(id) {
  const el = document.getElementById(id);
  if (el) el.innerHTML = '<p style="text-align:center;color:#888;padding:24px;">Loading...</p>';
}

function showError(id, msg) {
  const el = document.getElementById(id);
  if (el) el.innerHTML = `<p style="color:red;text-align:center;padding:24px;">${msg}</p>`;
}

// Minimal PWA shell; wire WebLLM here (import from CDN or local bundle)
// Note: For offline-first, cache the assets via service worker and pre-download model shards.
const out = document.getElementById('out');
document.getElementById('run').onclick = async () => {
  const prompt = document.getElementById('prompt').value.trim();
  if (!prompt) return;
  out.textContent += `\n> ${prompt}\n`;
  // TODO: integrate WebLLM session and stream tokens
  out.textContent += `[stub] WebLLM response here...\n`;
};
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('./service-worker.js');
}

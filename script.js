document.getElementById("interestForm").addEventListener("submit", function(event) {
  event.preventDefault();

  let P = parseFloat(document.getElementById("principal").value);
  let R = parseFloat(document.getElementById("rate").value);
  let T = parseFloat(document.getElementById("time").value);

  let SI = (P * R * T) / 100;

  document.getElementById("result").textContent = SI.toFixed(2);
});


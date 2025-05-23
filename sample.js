const word_a = "朝から驚きの連続だ";
const word_i = "いつもの朝とは様子が違う";
const word_u = "嬉しい知らせが飛び込んできた";
const word_e = "駅で急に待ち合わせ。慌てて準備して";
const word_o = "温泉旅行に出発だ！";

const outputDiv = document.getElementById("output");
outputDiv.innerHTML = `
    <p>あ：${word_a}</p>
    <p>い：${word_i}</p>
    <p>う：${word_u}</p>
    <p>え：${word_e}</p>
    <p>お：${word_o}</p>
`;
function updateClock() {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  const timeString = `${hours}:${minutes}:${seconds}`;
  document.getElementById('clock').textContent = timeString;
}

updateClock(); // 初期表示
setInterval(updateClock, 1000); // 毎秒更新
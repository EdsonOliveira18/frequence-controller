// Carrossel com suporte à múltiplos slides (se você adicionar mais no futuro)
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
  slides.forEach((slide, idx) => {
    slide.classList.toggle('active', idx === index);
  });
}

// Avança slide para o próximo (substitui sua função original)
function nextSlide() {
  currentSlide = (currentSlide + 1) % slides.length;
  showSlide(currentSlide);
}

// Retorna ao slide anterior (opcional, caso queira navegação reversa)
function previousSlide() {
  currentSlide = (currentSlide - 1 + slides.length) % slides.length;
  showSlide(currentSlide);
}

// Navegação por teclas (opcional, mas útil)
document.addEventListener("keydown", (event) => {
  if(event.key === "ArrowRight") nextSlide();
  if(event.key === "ArrowLeft") previousSlide();
});

// Máscara automática de CPF ao digitar
document.getElementById("cpf").addEventListener("input", function () {
  let value = this.value.replace(/\D/g, "");
  value = value.replace(/(\d{3})(\d)/, "$1.$2");
  value = value.replace(/(\d{3})(\d)/, "$1.$2");
  value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
  this.value = value;
});

// Envio do formulário com validação, geolocalização e envio rápido (seu código ajustado)
document.getElementById("form-cpf").addEventListener("submit", async (e) => {
  e.preventDefault();

  const botaoEnviar = document.querySelector("#form-cpf button[type='submit']");
  botaoEnviar.disabled = true; // Evita cliques repetidos

  const agora = new Date();
  document.getElementById("horario").value = agora.toTimeString().slice(0, 5);

  navigator.geolocation.getCurrentPosition(async (pos) => {
    document.getElementById("localizacao").value = `${pos.coords.latitude},${pos.coords.longitude}`;

    const body = {
      cpf: document.getElementById("cpf").value,
      horario: document.getElementById("horario").value,
      local: document.getElementById("localizacao").value
    };

    try {
      const response = await fetch("http://localhost:8003/registrar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
      });

      const result = await response.json();
      document.getElementById("resultado").innerText = result.resultado;
    } catch (erro) {
      document.getElementById("resultado").innerText = "Erro na requisição ao servidor.";
      console.error(erro);
    } finally {
      botaoEnviar.disabled = false; // Libera botão após resposta
    }
  }, () => {
    document.getElementById("resultado").innerText = "Erro ao obter localização.";
    botaoEnviar.disabled = false;
  });
});

// Inicia no slide correto baseado na URL (opcional, recomendado se estiver usando QRCode que abre diretamente no formulário)
document.addEventListener("DOMContentLoaded", () => {
  const params = new URLSearchParams(window.location.search);
  if(params.get('slide') === 'form') {
    currentSlide = 1; // formulário é o segundo slide
  } else {
    currentSlide = 0; // padrão é o QRCode
  }
  showSlide(currentSlide);
});

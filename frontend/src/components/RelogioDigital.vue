<template>
  <div class="relogio-digital">
    {{ hora }}
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'

const hora = ref('')

function atualizarHora() {
  const agora = new Date()
  hora.value = agora.toLocaleTimeString('pt-BR', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  })
}

let intervalo: number

onMounted(() => {
  atualizarHora()
  intervalo = setInterval(atualizarHora, 1000)
})

onBeforeUnmount(() => {
  clearInterval(intervalo)
})
</script>

<style scoped>
.relogio-digital {
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bolder;
  font-family: monospace;
  font-size: 3rem;
  color: #000000;
  background-color: #ffffff;
  padding: 1.5rem 2rem;
  border: 3px solid #000000;
  border-radius: 50%;
  box-shadow: none;
  height: 16rem;
  width: fit-content;
}
</style>

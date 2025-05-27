<template>
  <div class="tela">
    <!-- Cabeçalho fixo -->
    <header class="cabecalho">
      <h1 class="titulo">Painel do Administrador</h1>
    </header>

    <!-- Conteúdo centralizado -->
    <div class="PainelBotoes">
      <Button
          class="botaoQuadrado"
          @click="mostrarModal = true">
          <div class="conteudoBotao">
              <i class="pi pi-user-plus"></i>
              <span>Novo Colaborador</span>
          </div>
      </Button>
      <Button class="botaoQuadrado" @click="mostrarLogin = true">
        <div class="conteudoBotao">
          <i class="pi pi-clock"></i>
          <span>Registro de Ponto</span>
        </div>
      </Button>
      <Button
          class="botaoQuadrado">
          <div class="conteudoBotao">
              <i class="pi pi-download"></i>
              <span>Exportar CSV</span>
          </div>
      </Button>

      <Dialog v-model:visible="mostrarModal" modal>
        <template #header>
          <h2 class="custom-dialog-title">Cadastro de Colaborador</h2>
        </template>

        <div class="dialog-content">
          <QrcodeVue
            :value="urlCadastro"
            :size="350"
            :level="'M'"
            class="mx-auto"
          />
          <p>Aponte a câmera do seu celular para o QR Code</p>
        </div>
      </Dialog>
    </div>
  <ModalLoginColaborador v-model:visible="mostrarLogin" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import QrcodeVue from 'qrcode.vue'
import ModalLoginColaborador from '@/components/ModalLoginColaborador.vue'

const mostrarLogin = ref(false)
const mostrarModal = ref(false)
const VITE_PUBLIC_APP_URL = import.meta.env.VITE_PUBLIC_APP_URL
const urlCadastro = `${VITE_PUBLIC_APP_URL}/cadastro`
</script>

<style scoped>
.tela {
  display: flex;
  flex-direction: column;
  height: 90vh;
  background-color: #f9fafb;
}

.cabecalho {
  padding: 1rem;
  text-align: center;
  border-bottom: 2px solid #e5e7eb; /* borda inferior leve */
}

.titulo {
  font-size: 2rem;
  font-weight: 600;
  font-family: 'Inter', sans-serif;
  margin: 0;
}

.PainelBotoes {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5rem;
}

.botaoQuadrado {
  border-radius: 2px !important;
  height: 30rem;
  width: 20rem;
  padding: 0.75rem 1.5rem;
  font-size: 20px;
  font-family: 'Calibri';

  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.conteudoBotao {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}

.botaoQuadrado i {
  font-size: 8rem; /* Tamanho grande do ícone */
}

.custom-dialog-title {
  font-family: Arial !important;
  font-weight: bold;
  text-align: center;
  margin: 0;
}

.dialog-content {
  font-family: Arial !important;
  font-size: 1rem !important;
  padding-left: 1rem;
  padding-right: 1rem;
}

.dialog-content p {
    font-size: 1rem;
  padding-top: 1rem;
}
</style>

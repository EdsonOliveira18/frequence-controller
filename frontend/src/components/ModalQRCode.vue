<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg shadow-lg p-6 w-full max-w-md text-center relative">
      <button
        @click="$emit('fechar')"
        class="absolute top-2 right-2 text-gray-500 hover:text-red-500 text-xl"
        title="Fechar"
      >
        &times;
      </button>

      <h2 class="text-xl font-bold mb-4">Escaneie para se cadastrar</h2>

      <qrcode-vue
        :value="urlCadastro"
        :size="200"
        :level="'M'"
      />
      <p class="text-sm text-gray-500 mt-4">Aponte a câmera do seu celular para o QR Code</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import QrcodeVue from 'qrcode.vue'

const urlCadastro = `${import.meta.env.VITE_PUBLIC_APP_URL}/cadastro`
</script>

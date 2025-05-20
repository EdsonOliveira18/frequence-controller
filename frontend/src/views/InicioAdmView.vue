<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-gray-100">
    <h1 class="text-3xl font-bold mb-8">Painel do Administrador</h1>

    <button
      @click="mostrarModal = true"
      class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded"
    >
      + Novo Colaborador
    </button>

    <!-- Modal QRCode -->
    <ModalQRCode v-if="mostrarModal" @fechar="mostrarModal = false" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ModalQRCode from '@/components/ModalQRCode.vue'

const mostrarModal = ref(false)
</script>

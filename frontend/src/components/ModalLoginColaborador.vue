<template>
  <Dialog
    v-model:visible="modelVisible"
    modal
    appendTo="body"
    :style="{ width: '400px', height: '600px' }"
    :pt="ptDialog">
    <div class="login-container">
      <h2 class="login-title">Registro de Ponto</h2>

      <div class="form-group">
        <label for="cpf">CPF</label>
        <InputMask 
          id="cpf"
          name="registro_ponto_usuario"
          v-model="cpf"
          mask="999.999.999-99"
          class="login-input"
          autocomplete="off"
          autocapitalize="off"
          spellcheck="false"
  />
      </div>

      <div class="form-group">
        <label for="senha">Senha</label>
        <Password 
          v-model="senha"
          inputId="senha"
          toggleMask
          class="login-input"
          autocomplete="off" />
      </div>
      <Button type="button" label="Registrar Ponto" class="login-button" @click="handleLogin" :disabled="!formularioValido" />
    </div>
  </Dialog>
  <Dialog
    v-model:visible="mostrarResultado"
    modal
    class="dialog-resultado"
    :style="{ width: '400px', height: '650px' }"
    :pt="ptDialog">
  <div class="msg-container">
    <h3 class="rgt-title">Registro de Ponto</h3>
    <RelogioDigital />
    <div class="msg-container-parag">
        <p>{{ mensagem }}</p>
        <p style="font-weight: bold; font-family: Arial; font-size: 1.2rem;">
          Fechando em {{ contador }} segundo<span v-if="contador !== 1">s</span>...
        </p>
    </div>
  </div>
  </Dialog>
</template>

<script setup lang="ts">
import { nextTick } from 'vue'
import { defineProps, defineEmits, computed, ref, watch } from 'vue'
import Dialog from 'primevue/dialog'
import InputMask from 'primevue/inputmask'
import Password from 'primevue/password'
import Button from 'primevue/button'
import Message from 'primevue/message'
import { loginColaborador, registrarPonto } from '@/services/api'
import RelogioDigital from "./RelogioDigital.vue";


const colaborador = ref(null)
const mensagem = ref('')
const mostrarResultado = ref(false)

const contador = ref(15)
let intervalo: ReturnType<typeof setInterval> | null = null

const props = defineProps<{ visible: boolean }>()
const emit = defineEmits<{
  (e: 'update:visible', value: boolean): void
}>()

const ptDialog = {
  header: {
    style: 'padding-top: 1rem; padding-bottom: 0; padding-left: 1rem; padding-right: 1rem; display: flex; justify-content: flex-end;'
  }
};

const modelVisible = computed({
  get: () => props.visible,
  set: (value) => emit('update:visible', value),
})

const cpf = ref('')
const senha = ref('')

const formularioValido = computed(() => cpf.value.replace(/\D/g, '').length === 11 && senha.value.trim().length >= 4)

watch(mostrarResultado, (visivel) => {
  if (!visivel) {
    modelVisible.value = false
    // Quando o Dialog de resultado é fechado manualmente, limpar o contador
    if (intervalo) {
      clearInterval(intervalo)
      intervalo = null
    }
    contador.value = 15
  }
})

async function handleLogin() {
  try {
    const response = await loginColaborador(cpf.value, senha.value)

    colaborador.value = response 

    console.log('Colaborador autenticado:', colaborador.value)
    console.log('Enviando para registrar ponto com ID:', colaborador.value.id_col)

    const registro = await registrarPonto(colaborador.value.id_col)

    const hora = new Date(registro.timestamp_reg).toLocaleTimeString('pt-BR', {
      hour: '2-digit',
      minute: '2-digit'
    })

    mensagem.value = `${colaborador.value.nome_col}, seu ponto de ${registro.tipo_reg} foi registrado às ${hora}`
    mostrarResultado.value = true

    cpf.value = ''
    senha.value = ''

    contador.value = 15
    intervalo = setInterval(() => {
    contador.value--
    if (contador.value === 0) {
      clearInterval(intervalo!)
      mostrarResultado.value = false
      modelVisible.value = false
    }
    }, 1000)
    
    // // ✅ Apenas após sucesso
    // setTimeout(() => {
    //   mostrarResultado.value = false
    //   modelVisible.value = false // Fecha Dialog principal
    // }, 15000) //15 segundos

  } catch (error: any) {
    console.error('Erro no login ou registro de ponto:', error)
    cpf.value = ''
    senha.value = ''

    if (error.response) {
      console.log('Status:', error.response.status)
      console.log('Data:', error.response.data)
    }

    mensagem.value = '❌ Erro ao registrar ponto. Verifique CPF e senha.'
    mostrarResultado.value = true
    console.log(colaborador.value)
  }
}

</script>

<style>
.dialog-resultado .p-dialog-content {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>

<style scoped>

.login-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 1rem;
}

.msg-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  padding: 1rem;
  gap: 2rem;
  width: fit-content;
}

.msg-container-parag {
  justify-content: center;
  font-family: Arial;
}

.login-title {
  text-align: center;
  font-size: 3rem;
  font-weight: bold;
  font-family: Arial;
  margin-bottom: 0.5rem;
}

.rgt-title {
  text-align: center;
  font-size: 2rem;
  font-weight: bold;
  font-family: Arial;
  margin-bottom: 0rem;
}

.form-group {
  font-family: Arial;
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.login-input {
  width: 100%;
}

.login-button {
  font-family: Arial;
  width: 100%;
  margin-top: 1rem;
  background-color: #17a2b8;
  border: none;
}

.login-msg {
  margin-top: 1rem;
  text-align: center;
}

</style>

<template>
  <div class="tela">
    <!-- Cabeçalho -->
    <header class="cabecalho">
      <h1 class="titulo">Cadastro de Colaborador</h1>
    </header>

    <!-- Formulário -->
    <div class="conteudo">
      <form @submit.prevent="handleSubmit" class="espaco-form">
        <div class="campo-form">
          <label for="nome">Nome Completo</label>
          <InputText id="nome" v-model="form.nome" class="input-prime" required />
        </div>

        <div class="campo-form">
          <label for="cpf">CPF</label>
          <InputMask
            id="cpf"
            v-model="form.cpf"
            mask="999.999.999-99"
            class="input-prime"
            required
          />
        </div>

        <div class="campo-form">
          <label for="email">Email</label>
          <InputText id="email" v-model="form.email" type="email" class="input-prime" required />
        </div>
        <div class="campo-botao">
            <Button type="submit" icon="pi pi-save" class="BotaoCad" :disabled="!formularioValido">Cadastrar</Button>
        </div>
      </form>
      <br>
      <!-- Mensagem de sucesso -->
      <Message
        v-if="senhaGerada"
        severity="success"
        class="mt-4"
      >
        <p>Cadastro realizado com sucesso!</p>
        <p>SUA SENHA: <strong>{{ senhaGerada }}</strong></p>
        <br>
        <Card class="card_css">
            <template #title><div class="alerta">!!! ATENÇÃO !!!</div></template>
            <template #content>
                <p class="destaque">Anote essa senha. Ela não será exibida novamente! Recomendamos que você tire PRINT da sua tela.</p>
            </template>
        </Card>
      </Message>

      <!-- Mensagem de erro -->
      <Message
        v-if="erro"
        severity="error"
        class="mt-4"
      >
        {{ erro }}
      </Message>
    </div>
    <!-- Diálogo de Erro -->
    <Dialog v-model:visible="mostrarDialogErro" modal header="Erro ao cadastrar" class="w-11/12 sm:w-96">
      <p class="text-red-700">{{ erro }}</p>
      <p class="text-sm mt-2">Por favor, revise os dados e tente novamente.</p>
    </Dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import Card from 'primevue/card';
import InputMask from 'primevue/inputmask'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import { cadastrarColaborador } from '@/services/api'

interface FormularioCadastro {
  nome: string
  cpf: string
  email: string
}

const form = ref<FormularioCadastro>({
  nome: '',
  cpf: '',
  email: '',
})

const senhaGerada = ref('')
const erro = ref('')
const mostrarDialogErro = ref(false)

const formularioValido = computed(() =>
  form.value.nome.trim() !== '' &&
  form.value.cpf.replace(/\D/g, '').length === 11 &&
  form.value.email.trim() !== ''
)

const copiarSenha = async () => {
  try {
    await navigator.clipboard.writeText(senhaGerada.value)
    alert('Senha copiada para a área de transferência!')
  } catch {
    alert('Erro ao copiar senha.')
  }
}

const handleSubmit = async () => {
  erro.value = ''
  senhaGerada.value = ''
  mostrarDialogErro.value = false
  mostrarDialogSucesso.value = false

  try {
    const resposta = await cadastrarColaborador(form.value)
    senhaGerada.value = resposta.senha_gerada
    mostrarDialogSucesso.value = true
  } catch (err: any) {
    erro.value = err?.response?.data?.detail || 'Erro ao cadastrar colaborador.'
    mostrarDialogErro.value = true
  }
}
</script>

<style scoped>
.tela {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #f9fafb;
}

.cabecalho {
  color: black;
  padding: 1rem;
  text-align: center;
  border-bottom: 2px solid #e5e7eb;
}

.titulo {
  font-size: 1.8rem;
  font-weight: 600;
  font-family: 'Inter', sans-serif;
  margin: 0;
}

.conteudo {
  font-family: Arial;
  color: black;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 1.5rem;
}

.espaco-form {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.campo-form label {
  font-weight: 500;
  font-size: 0.95rem;
  margin-bottom: 0.25rem;
  display: block;
}

.input-prime {
  color: black;
  border-color: #d5d5d5;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
  background-color: rgb(246, 246, 246);
  width: 100%;
}

.campo-botao {
  display: flex;
  justify-content: center; /* horizontal */
  align-items: center;     /* vertical */
}

.BotaoCad {
  width: 50%;
  color: white;
  font-family: Arial;
  font-size: 1rem;
  margin-bottom: 0.25rem;
  display: block;
}

.aviso-msg {
  font-family: Arial;
  display:grid;
  justify-content: center;
  align-items: center;
}

.aviso-msg h2 {
  color: red;
}

.card_css {
  background: #000000;
  color: rgb(255, 255, 255);
}

.alerta {
  /* text-shadow: 0 2px 6px rgb(255, 0, 0); */
  color: red;
  font-weight: bold;
  font-size: 24px;
}

.destaque {
  /* text-shadow: 0 2px 6px rgb(255, 255, 255); */
  text-align: justify;
  font-size:medium;
  font-weight: bold;
}
</style>

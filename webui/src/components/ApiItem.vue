<template>
  <div class="accordion-item rounded-0">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed rounded-0"
              type="button"
              data-bs-toggle="collapse"
              :data-bs-target="'#' + itemId"
              aria-expanded="false"
              aria-controls="collapseThree">
        <span class="d-flex align-items-center column-gap-2">
          <span class="py-1 px-3 rounded-1 text-white"
                :class="getMethodClass(data.method)">
            {{ data.method }}
          </span>
          <strong>{{ data.path }}</strong>
          <span class="fw-light">{{ data.summary }}</span>
        </span>
      </button>
    </h2>
    <div :id="itemId"
         class="accordion-collapse collapse">
      <div class="accordion-body">
        <h5>Parameters</h5>
        <div class="table table-responsive">
          <table class="table">
            <thead>
            <tr>
              <th>Name</th>
              <th>Description</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="parameter in data.parameters">
              <td>
                <div class="d-flex flex-column">
                  <span>
                    <b>{{ parameter.name }}</b>
                    <small v-if="parameter.required" class="text-danger ms-1">* required</small>
                  </span>
                  <small>{{ parameter.type }}</small>
                  <small class="text-body-tertiary fw-light fst-italic">({{ parameter.in }})</small>
                </div>
              </td>
              <td>
                {{ parameter.description }}
                <span v-if="parameter.default">(<b>default</b>: {{parameter.default}})</span>
              </td>
            </tr>
            </tbody>
          </table>
        </div>

        <h5>Responses</h5>
        <div class="table table-responsive">
          <table class="table">
            <thead>
            <tr>
              <th>Code</th>
              <th>Description</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="response in data.responses">
              <td class="fw-bold">{{ response.code }}</td>
              <td>
                <div class="d-flex flex-column">
                  <span>
                    {{ response.description }}
                  </span>
                  <small>Example:</small>
                  <pre class="text-bg-dark p-2 rounded-1 mt-1">{{ response.example }}</pre>
                </div>
              </td>

            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>

import {computed} from "vue";

const props = defineProps({
  uuid: {
    type: Number,
    require: true
  },
  data: {
    type: Object,
    required: true
  }
})

const itemId = computed(() => `collapse-${props.uuid}`)
const getMethodClass = (method) => {
  switch (method) {
    case 'GET':
      return 'bg-primary';
    case 'POST':
      return 'bg-success';
    case 'DELETE':
      return 'bg-danger';
    case 'PUT':
      return 'bg-warning';
    case 'PATCH':
      return 'bg-warning';
    default:
      return ''
  }
}
</script>

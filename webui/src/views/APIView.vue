<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 col-lg-9 mx-auto py-4">
        <header class="d-flex align-items-center pb-3 mb-5 border-bottom text-center flex-column fw-bold">
          <h1>Sahibin API</h1>
          <p class="text-secondary fw-light">
            Empowering Snippet Integration!
          </p>
        </header>
        <main>
          <h3 class="pb-3 my-3">Introducing Sahibin API</h3>
          <p>
            This comprehensive guide provides developers with all the information they need to integrate Sahibin's
            powerful snippet storage and sharing capabilities into their own applications. With Sahibin API, you can
            seamlessly retrieve paste content by key using a simple GET request, or create new pastes by making a POST
            request with the desired key and content. Whether you're building a code collaboration tool, a documentation
            system, or any application that requires efficient snippet management, Sahibin API empowers you with the
            tools to enhance your application's functionality. Explore the documentation below to unleash the full
            potential of Sahibin API and elevate your development experience.
          </p>
          <hr class="col-5 mb-5">

          <h3>API Guide</h3>
          <p class="lead">Sahibin API</p>
          <div class="accordion">
            <api-item v-for="(item, index) in endpoints" :key="index" :data="item" :uuid="index"/>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import ApiItem from "@/components/ApiItem.vue";
import {onMounted} from "vue";
import {setupBootstrap} from "@/plugins";

const endpoints = [
  {
    path: '/api/get',
    method: 'GET',
    summary: 'Get Paste content by key',
    parameters: [
      {
        name: 'key',
        in: 'query',
        required: true,
        description: 'The paste key to retrieve',
        default: null,
        type: 'string',
      }
    ],
    responses: [
      {
        code: '200',
        description: 'Return a successful result when paste with key exists',
        example: '{ "data": "Paste content" }'
      },
      {
        code: '404',
        description: 'Return an unsuccessful result when paste with key does not exists',
        example: '{ "detail": "Paste not found" }'
      },
    ]
  },
  {
    path: '/api/raw',
    method: 'GET',
    summary: 'Get Paste content by key as raw',
    parameters: [
      {
        name: 'key',
        in: 'query',
        required: true,
        description: 'The paste key to retrieve',
        default: null,
        type: 'string',
      }
    ],
    responses: [
      {
        code: '200',
        description: 'Return a successful result when paste with key exists',
        example: 'Paste content'
      },
      {
        code: '404',
        description: 'Return an unsuccessful result when paste with key does not exists',
        example: 'Paste not found'
      },
    ]
  },
  {
    path: '/api/create',
    method: 'POST',
    summary: 'Create new paste',
    parameters: [
      {
        name: 'key',
        in: 'body',
        required: false,
        description: 'The paste key',
        default: 'An unique uuid',
        type: 'string',
      },
      {
        name: 'data',
        in: 'body',
        required: true,
        description: 'The paste content',
        default: null,
        type: 'string',
      }
    ],
    responses: [
      {
        code: '201',
        description: 'Return a successful result when paste created',
        example: '{ "key": "f09781ec-0e39-4c52-80fc-1fd9f0e9f935" }'
      },
      {
        code: '409',
        description: 'Return conflict result when paste with key already exists',
        example: '{ "detail": "A paste with key {key} already exists" }'
      },
    ]
  },
]

onMounted(() => setupBootstrap())
</script>


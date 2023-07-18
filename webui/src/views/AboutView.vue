<template>
  <div class="container-lg">
    <div class="row">
      <div class="col-12 mx-auto py-4">
        <header class="d-flex align-items-center pb-3 mb-5 border-bottom text-center flex-column fw-bold">
          <h1>Sahibin</h1>
          <p class="text-secondary fw-light">
            Your Reliable Snippet Storage and Sharing Platform
          </p>
        </header>
        <main>
          <h3 class="text-body-emphasis">Introducing Sahibin</h3>
          <p class="fs-6 col-12">
            Sahibin is an innovative online platform designed to simplify the process of storing and sharing plain text
            or code snippets. With its user-friendly interface and powerful features, Sahibin empowers developers,
            programmers, and users in general to conveniently save, access, and distribute their valuable text-based
            content. Whether you're looking to organize your code snippets, share useful information with others, or
            simply keep track of important notes, Sahibin is the go-to tool for all your snippet management needs.
          </p>
          <hr class="col-5 mb-5">

          <div class="row g-1">
            <div class="col-12">
              <h3>Development</h3>
              <p>
                Sahibin has been developed using cutting-edge technologies to ensure a seamless user experience
                (
                <a class="link-underline" target="_blank"
                   href="https://github.com/ozcanyarimdunya/sahibin">
                  Source code
                </a>
                ).
              </p>
            </div>
            <div class="col-12 col-md-4">
              <h5>Backend</h5>
              <p>
                The backend of the platform is built with FastAPI, a high-performance web framework for Python, which
                guarantees speedy and efficient processing of user requests.
              </p>
            </div>
            <div class="col-12 col-md-4">
              <h5>Frontend</h5>
              <p>
                The frontend of the platform is built with Vue.js, a progressive JavaScript framework, provides a
                responsive and intuitive interface, allowing users to interact with Sahibin effortlessly.
              </p>
            </div>
            <div class="col-12 col-md-4">
              <h5>Database</h5>
              <p>
                The platform's data is securely stored in a MongoDB database, ensuring reliability and scalability.
              </p>
            </div>
          </div>
          <hr class="col-5 mb-5">

          <div class="row g-1">
            <div class="col-12">
              <h3>Command-Line Interface (CLI) for Quick Snippet Management</h3>
              <p>
                To further enhance accessibility and convenience, Sahibin offers a command-line interface (CLI) that
                enables users to interact with the platform directly from their terminal. By leveraging the CLI, users
                can effortlessly create snippets by providing content through standard input (stdin).
              </p>
              <router-link :to="{name: 'cli'}" class="btn btn-primary">Install Sahibin CLI</router-link>
            </div>
          </div>
          <hr class="col-5 mb-5">

          <div class="row g-1">
            <div class="col-12">
              <h3>API Integration for Seamless Integration</h3>
              <p>
                Sahibin provides a simple yet powerful API that allows developers to integrate snippet creation and
                retrieval functionality into their applications.
              </p>
              <router-link :to="{name: 'docs'}" class="btn btn-outline-primary">API Documentation</router-link>
            </div>
          </div>
          <hr class="col-5 mb-5">
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
</style>

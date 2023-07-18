<template>
  <div class="container-lg">
    <div class="row">
      <div class="col-12 mx-auto py-4">
        <header class="d-flex align-items-center pb-3 mb-5 border-bottom text-center flex-column fw-bold">
          <h1>Sahibin CLI</h1>
          <p class="text-secondary fw-light">
            Share Effortlessly!
          </p>
        </header>
        <main>
          <h3 class="pb-3 my-3">Introducing Sahibin CLI</h3>
          <p>
            Sahibin CLI is a command-line interface tool designed to seamlessly integrate with the Sahibin platform,
            offering a convenient way to create text or code snippets directly from the terminal. With Sahibin CLI,
            developers and users can effortlessly store and share their valuable content without the need to switch to a
            web browser or navigate through a graphical user interface. By providing a set of intuitive commands and
            options, Sahibin CLI streamlines the process of creating snippets by allowing users to input content
            directly or via standard input. Whether it's quickly saving and sharing code snippets or accessing content
            from shared URLs, Sahibin CLI offers a command-line experience that enhances productivity and efficiency.
          </p>
          <p>
            Powered by Sahibin's robust backend infrastructure, Sahibin CLI ensures reliable and secure interactions
            with the Sahibin platform. Users can rely on Sahibin CLI to create snippets with ease, whether it's
            single-line code snippets or multi-paragraph text content. With its simplicity, flexibility, and powerful
            features, Sahibin CLI is a valuable tool for developers, programmers, and users looking to efficiently
            manage their text-based content and collaborate effectively within their command-line environments.
          </p>
          <hr class="col-5 mb-5">

          <h3>Installation Guide</h3>
          <p class="lead">Follow these steps to install Sahibin CLI on macOS and Linux:</p>
          <div class="container border">
            <div class="row">
              <div class="col py-3">
                <ol>
                  <li>Open the Terminal application on your Mac and Linux machine.</li>
                  <li>
                    Check if you have
                    <strong>
                      <a href="https://www.python.org/downloads/" target="_blank">python3</a>
                    </strong> installed and once it is installed, run the following command to install Sahibin CLI:
                    <simple-code :content="`sudo curl -k ${url}/sahibin -o /usr/local/bin/sahibin`"/>
                    <simple-code content="sudo chmod +x /usr/local/bin/sahibin"/>
                  </li>
                  <li>
                    Verify the installation by running the following command:
                    <simple-code content="sahibin --version" :output="packageJson.version"/>
                    <p>You should see the version number of Sahibin CLI if it was installed successfully.</p>
                  </li>
                </ol>
                <div class="alert alert-danger mt-4 mx-1" role="alert">
                  Sahibin CLI uses <b>SAHIBIN_URL</b> environment variable as base url.
                  You can change the base url by running following command:
                  <simple-code :content='`export SAHIBIN_URL="${url}"`'/>
                </div>
              </div>
            </div>
          </div>
          <div class="mb-5"></div>

          <h3>Usage Guide</h3>
          <p class="lead">Follow these examples to effectively use Sahibin CLI:</p>
          <div class="card rounded-0">
            <div class="card-body">
              <h5 class="card-title">Create a new paste by providing content directly.</h5>
              <p class="card-text">
                This command get content as argument then creates a new paste and print paste's shareable URL to the
                console.
              </p>
              <simple-code content="sahibin 'a simple content'" :output="`${url}/share/a-unique-key`"/>
            </div>
            <div class="card-body">
              <h5 class="card-title">Create a new paste by providing content via stdin.</h5>
              <p class="card-text">
                This command get content via stdin then creates a new paste and print paste's shareable URL to the
                console.
              </p>
              <simple-code content="echo 'content from stdin' | sahibin " :output="`${url}/share/a-unique-key`"/>
            </div>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import packageJson from '@/../package.json';
import SimpleCode from "@/components/SimpleCode.vue";

const url = window.location.origin;
</script>

<style scoped>
</style>

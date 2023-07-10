<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 col-lg-9 mx-auto py-4">
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
            offering a convenient way to create, retrieve, and manage text or code snippets directly from the terminal.
            With Sahibin CLI, developers and users can effortlessly store and share their valuable content without the
            need to switch to a web browser or navigate through a graphical user interface. By providing a set of
            intuitive commands and options, Sahibin CLI streamlines the process of creating snippets by allowing users
            to
            input content directly or via standard input. Additionally, it offers the flexibility to specify custom keys
            for snippets, making it easier to organize and retrieve specific snippets in the future. Whether it's
            quickly
            saving and sharing code snippets or accessing content from shared URLs, Sahibin CLI offers a command-line
            experience that enhances productivity and efficiency.
          </p>
          <p>
            Powered by Sahibin's robust backend infrastructure, Sahibin CLI ensures reliable and secure interactions
            with
            the Sahibin platform. Users can rely on Sahibin CLI to create snippets with ease, whether it's single-line
            code snippets or multi-paragraph text content. With the ability to retrieve snippet content by providing the
            full URL, Sahibin CLI enables seamless integration with other command-line tools and workflows. With its
            simplicity, flexibility, and powerful features, Sahibin CLI is a valuable tool for developers, programmers,
            and users looking to efficiently manage their text-based content and collaborate effectively within their
            command-line environments.
          </p>
          <hr class="col-5 mb-5">

          <h3>Installation Guide</h3>
          <p class="lead">Follow these steps to install Sahibin CLI on macOS and Linux:</p>
          <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active rounded-0"
                      id="macos-tab"
                      data-bs-toggle="tab"
                      data-bs-target="#macos"
                      type="button"
                      role="tab"
                      aria-controls="macos"
                      aria-selected="true">
                MacOS
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link rounded-0"
                      id="linux-tab"
                      data-bs-toggle="tab"
                      data-bs-target="#linux"
                      type="button"
                      role="tab"
                      aria-controls="linux"
                      aria-selected="false">
                Linux
              </button>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane active" id="macos" role="tabpanel" aria-labelledby="macos-tab" tabindex="0">
              <div class="container">
                <div class="row">
                  <div class="col border border-top-0 py-3">
                    <ol>
                      <li>Open the Terminal application on your Mac.</li>
                      <li>
                        Check if you have <strong>jq</strong> installed by running the following command:
                        <br>
                        <simple-code content="jq --version"/>
                        <span>
                        If <strong>jq</strong> is not installed, you can install it by running the following command:
                      </span>
                        <simple-code content="brew install jq"/>
                      </li>
                      <li>
                        Once <strong>jq</strong> is installed, run the following command to install Sahibin CLI:
                        <simple-code
                            content="sudo curl -k http://localhost:5000/api/raw?key=stable -o /usr/local/bin/sahibin"/>
                        <simple-code content="sudo chmod +x /usr/local/bin/sahibin"/>
                      </li>
                      <li>
                        Verify the installation by running the following command:
                        <simple-code content="sahibin --version" :output="packageJson.version"/>
                        <p>You should see the version number of Sahibin CLI if it was installed successfully.</p>
                      </li>
                    </ol>
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-pane" id="linux" role="tabpanel" aria-labelledby="linux-tab" tabindex="1">
              <div class="container">
                <div class="row">
                  <div class="col border border-top-0 py-3">
                    <ol>
                      <li>Open the Terminal application on your Linux machine.</li>
                      <li>
                        Check if you have <strong>jq</strong> installed by running the following command:
                        <br>
                        <simple-code content="jq --version"/>
                        <span>
                        If <strong>jq</strong> is not installed, you can install it by running the following command:
                      </span>
                        <simple-code content="sudo apt-get update"/>
                        <simple-code content="sudo apt-get install jq"/>
                      </li>
                      <li>
                        Once <strong>jq</strong> is installed, run the following command to install Sahibin CLI:
                        <simple-code
                            content="sudo curl -k http://localhost:5000/api/raw?key=stable -o /usr/local/bin/sahibin"/>
                        <simple-code content="sudo chmod +x /usr/local/bin/sahibin"/>
                      </li>
                      <li>
                        Verify the installation by running the following command:
                        <simple-code content="sahibin --version" :output="packageJson.version"/>
                        <p>You should see the version number of Sahibin CLI if it was installed successfully.</p>
                      </li>
                    </ol>
                  </div>
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
              <simple-code
                  content="sahibin 'a simple content'"
                  output="https://.../share?key=a-unique-key"/>
            </div>
            <hr class="col-4 mx-auto">
            <div class="card-body">
              <h5 class="card-title">Create a new paste by providing content via stdin.</h5>
              <p class="card-text">
                This command get content via stdin then creates a new paste and print paste's shareable URL to the
                console.
              </p>
              <simple-code
                  content="echo 'content from stdin' | sahibin "
                  output="https://.../share?key=a-unique-key"/>
            </div>
            <hr class="col-4 mx-auto">
            <div class="card-body">
              <h5 class="card-title">Create a new paste with a custom key.</h5>
              <p class="card-text">
                This command get key and content as argument then creates a new paste and print paste's shareable URL to
                the
                console.
              </p>
              <simple-code
                  content="sahibin -k my-key 'new content'"
                  output="https://.../share?key=my-key"/>
            </div>
            <hr class="col-4 mx-auto">
            <div class="card-body">
              <h5 class="card-title">Get the content of a paste by providing the full URL.</h5>
              <p class="card-text">
                This command get full shareable url as argument then print paste's content to the console.
              </p>
              <simple-code
                  content="sahibin https://.../share?key=my-key"
                  output="The paste's content"/>
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
</script>

<style scoped>
</style>

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
          <p class="lead">Follow these steps to install & upgrade Sahibin CLI on macOS and Linux:</p>
          <div class="container-fluid border">
            <div class="row">
              <div class="col py-3">
                <ol>
                  <li>Open the Terminal application on your Mac or Linux machine.</li>
                  <li>Ensure that python 3.7+ is installed.
                    <simple-code content="python3 --version" output="Python 3.7+"/>
                  </li>
                  <li>
                    Once python 3.7+ is installed, run the following commands to install Sahibin CLI:
                    <simple-code :content="`sudo curl -k ${url}/sahibin -o /usr/local/bin/sahibin`"/>
                    <simple-code content="sudo chmod +x /usr/local/bin/sahibin"/>
                  </li>
                  <li>
                    Verify the installation by running the following command:
                    <simple-code content="sahibin --version" output="x.y.z"/>
                    <p>You should see the version number of Sahibin CLI if it was installed successfully.</p>
                  </li>
                </ol>
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
                This command read file content then creates a new paste and print paste's shareable URL to the
                console.
              </p>
              <simple-code content="cat /path/to/file.txt | sahibin " :output="`${url}/share/a-unique-key`"/>
            </div>
            <div class="card-body">
              <h5 class="card-title">Create a new paste by providing expire days.</h5>
              <p class="card-text">
                This command creates a new paste with 10 days as expiration days and print paste's shareable URL to the
                console.
              </p>
              <simple-code content="sahibin -e 10 'Expire in 10 days'" :output="`${url}/share/a-unique-key`"/>
            </div>
            <div class="card-body">
              <h5 class="card-title">Create a new paste by providing title.</h5>
              <p class="card-text">
                This command creates a new paste with title and print paste's shareable URL to the console.
              </p>
              <simple-code content="echo 'Paste content' | sahibin -t 'simple title'"
                           :output="`${url}/share/a-unique-key`"/>
            </div>
          </div>
          <div class="mb-5"></div>

          <h3>Configuration Guide</h3>
          <p class="lead">Sahibin CLI uses below environment variables:</p>
          <div class="table-responsive">
            <table class="table table-bordered">
              <thead>
              <tr>
                <th scope="col">Environment Variable</th>
                <th scope="col">Description</th>
                <th scope="col">Default Value</th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <th scope="row">SAHIBIN_URL</th>
                <td>Base sahibin url</td>
                <td class="text-body-secondary"><code>http://0.0.0.0:8000</code></td>
              </tr>
              <tr>
                <th scope="row">SAHIBIN_EXPIRE_DAYS</th>
                <td>Paste expiration in days</td>
                <td class="text-body-secondary"><code>1</code></td>
              </tr>
              <tr>
                <th scope="row">SAHIBIN_CHECK_UPDATES</th>
                <td>Check update everytime Sahibin CLI run</td>
                <td class="text-body-secondary"><code>True</code></td>
              </tr>
              <tr>
                <th scope="row">SAHIBIN_SESSIONID</th>
                <td>
                  Unique identifier used to track and manage a user's current interactions and pastes on the platform.
                  <br>
                  <span>Your unique session id:</span>
                  <simple-code :content="sessionid"/>
                </td>
                <td class="text-body-secondary">
                  <code>null</code>
                </td>
              </tr>
              </tbody>
            </table>
          </div>

        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import SimpleCode from "@/components/SimpleCode.vue";
import {useCookie} from "@/utils";

const {get} = useCookie()
const url = window.location.origin;

const sessionid = get('user-session-id');
</script>

<style scoped>
</style>

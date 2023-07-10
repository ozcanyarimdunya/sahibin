<template>
  <nav class="navbar bg-sahibin-dark">
    <div class="container-fluid">
      <a class="navbar-brand sahibin-logo fw-bold px-2 py-1 rounded-1" href="/">sahibin</a>
      <div class="px-0"
           role="button"
           data-bs-toggle="offcanvas"
           data-bs-target="#offcanvasNavbarLight"
           aria-controls="offcanvasNavbarLight">
        <svg xmlns="http://www.w3.org/2000/svg"
             width="32"
             height="32"
             fill="var(--sahibin-light-color)"
             class="bi bi-list"
             viewBox="0 0 16 16">
          <path fill-rule="evenodd"
                d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
        </svg>
      </div>
      <div class="offcanvas offcanvas-end"
           tabindex="-1"
           id="offcanvasNavbarLight"
           aria-labelledby="offcanvasNavbarLightLabel">
        <div class="offcanvas-header bg-sahibin-dark py-2">
          <a class="navbar-brand sahibin-logo fw-bold px-2 py-1 rounded-1" href="/">sahibin</a>
          <div role="button" data-bs-dismiss="offcanvas" aria-label="Close">
            <svg xmlns="http://www.w3.org/2000/svg"
                 width="20"
                 height="20"
                 fill="#ffffff"
                 viewBox="0 0 16 16">
              <path
                  d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"/>
            </svg>
          </div>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav pe-1 ps-1">
            <li class="nav-item border-bottom">
              <router-link :to="{name: 'home'}" class="nav-link">
                <div data-bs-dismiss="offcanvas">Home</div>
              </router-link>
            </li>
            <li class="nav-item border-bottom">
              <router-link :to="{name: 'about'}" class="nav-link">
                <div data-bs-dismiss="offcanvas">About</div>
              </router-link>
            </li>
            <li class="nav-item border-bottom">
              <router-link :to="{name: 'sahibin-cli'}" class="nav-link">
                <div data-bs-dismiss="offcanvas">Sahibin CLI</div>
              </router-link>
            </li>
            <li class="nav-item border-bottom">
              <router-link :to="{name: 'sahibin-api'}" class="nav-link">
                <div data-bs-dismiss="offcanvas">API Docs</div>
              </router-link>
            </li>
          </ul>
        </div>
        <div class="bg-light text-secondary d-flex align-items-center justify-content-center py-2 px-3 mt-auto">
          <small>Sahibin v{{ packageJson.version }} <b>@</b> 2023</small>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import packageJson from '@/../package.json'
</script>

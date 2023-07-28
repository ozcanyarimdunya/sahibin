<template>
  <nav class="navbar bg-sahibin-dark">
    <div class="container-lg">
      <a class="navbar-brand sahibin-logo fw-bold p-0 rounded-1" href="/">sahibin</a>
      <div class="d-flex column-gap-2 align-items-center">
        <router-link :to="{name: 'home'}"
                     class="d-flex align-items-center px-1 text-sahibin-light"
                     data-bs-toggle="tooltip"
                     data-bs-title="New Paste"
                     data-bs-placement="bottom">
          <svg xmlns="http://www.w3.org/2000/svg"
               width="20"
               height="20"
               fill="currentColor"
               viewBox="0 0 16 16">
            <path
                d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
            <path
                d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
          </svg>
        </router-link>
        <router-link :to="{name: 'history'}"
                     :class="{'text-white': isHere('history')}"
                     class="d-flex align-items-center px-1 text-sahibin-light"
                     data-bs-toggle="tooltip"
                     data-bs-title="History"
                     data-bs-placement="bottom">
          <svg xmlns="http://www.w3.org/2000/svg"
               width="20"
               height="20"
               fill="currentColor"
               viewBox="0 0 20 20">
            <path
                d="M10.5,0 C7,0 3.9,1.9 2.3,4.8 L0,2.5 L0,9 L6.5,9 L3.7,6.2 C5,3.7 7.5,2 10.5,2 C14.6,2 18,5.4 18,9.5 C18,13.6 14.6,17 10.5,17 C7.2,17 4.5,14.9 3.4,12 L1.3,12 C2.4,16 6.1,19 10.5,19 C15.8,19 20,14.7 20,9.5 C20,4.3 15.7,0 10.5,0 L10.5,0 Z M9,5 L9,10.1 L13.7,12.9 L14.5,11.6 L10.5,9.2 L10.5,5 L9,5 L9,5 Z"/>
          </svg>
        </router-link>
        <router-link :to="{name: 'cli'}"
                     :class="{'text-white': isHere('cli')}"
                     class="d-flex align-items-center px-1 text-sahibin-light"
                     data-bs-toggle="tooltip"
                     data-bs-title="Sahibin CLI"
                     data-bs-placement="bottom">
          <svg xmlns="http://www.w3.org/2000/svg"
               width="20"
               height="20"
               fill="currentColor"
               viewBox="0 0 16 16">
            <path
                d="M0 3a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3zm9.5 5.5h-3a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1zm-6.354-.354a.5.5 0 1 0 .708.708l2-2a.5.5 0 0 0 0-.708l-2-2a.5.5 0 1 0-.708.708L4.793 6.5 3.146 8.146z"/>
          </svg>
        </router-link>
        <div class="px-0"
             role="button"
             data-bs-toggle="offcanvas"
             data-bs-target="#offcanvasNavbarLight"
             aria-controls="offcanvasNavbarLight">
          <svg xmlns="http://www.w3.org/2000/svg"
               width="28"
               height="28"
               fill="var(--sahibin-light-color)"
               class="bi bi-list"
               viewBox="0 0 16 16">
            <path fill-rule="evenodd"
                  d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
          </svg>
        </div>
      </div>
      <div class="offcanvas offcanvas-end"
           tabindex="-1"
           id="offcanvasNavbarLight"
           aria-labelledby="offcanvasNavbarLightLabel">
        <div class="offcanvas-header bg-sahibin-dark py-2">
          <a class="navbar-brand sahibin-logo fw-bold p-0 rounded-1" href="/">sahibin</a>
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
            <li class="nav-item border-bottom" data-bs-dismiss="offcanvas">
              <router-link :to="{name: 'home'}" class="nav-link">
                <div>Home</div>
              </router-link>
            </li>
            <li class="nav-item border-bottom" data-bs-dismiss="offcanvas">
              <router-link :to="{name: 'about'}" class="nav-link">
                <div>About</div>
              </router-link>
            </li>
            <li class="nav-item border-bottom" data-bs-dismiss="offcanvas">
              <router-link :to="{name: 'history'}" class="nav-link">
                <div>History</div>
              </router-link>
            </li>
            <li class="nav-item border-bottom" data-bs-dismiss="offcanvas">
              <router-link :to="{name: 'cli'}" class="nav-link">
                <div>Sahibin CLI</div>
              </router-link>
            </li>
            <li class="nav-item border-bottom" data-bs-dismiss="offcanvas">
              <router-link :to="{name: 'docs'}" class="nav-link">
                <div>API Docs</div>
              </router-link>
            </li>
          </ul>
        </div>
        <div class="bg-light text-secondary d-flex align-items-center justify-content-between py-2 px-3 mt-auto">
          <small class="fw-medium">@ozcanyarimdunya</small>
          <small>v{{ packageJson.version }}</small>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import packageJson from '@/../package.json'
import {useRoute, useRouter} from "vue-router";

const router = useRouter()
const route = useRoute()

const isHere = (name) => route.name === name;
</script>


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
          <i class="bi bi-plus-square fs-5"></i>
        </router-link>
        <router-link :to="{name: 'history'}"
                     :class="{'text-white': isHere('history')}"
                     class="d-flex align-items-center px-1 text-sahibin-light"
                     data-bs-toggle="tooltip"
                     data-bs-title="History"
                     data-bs-placement="bottom">
          <i class="bi bi-clock-history fs-5"></i>
        </router-link>
        <router-link :to="{name: 'cli'}"
                     :class="{'text-white': isHere('cli')}"
                     class="d-flex align-items-center px-1 text-sahibin-light"
                     data-bs-toggle="tooltip"
                     data-bs-title="Sahibin CLI"
                     data-bs-placement="bottom">
          <i class="bi bi-terminal fs-5"></i>
        </router-link>
        <div class="p-0 text-sahibin-light"
             role="button"
             data-bs-toggle="offcanvas"
             data-bs-target="#offcanvasNavbarLight"
             aria-controls="offcanvasNavbarLight">
          <i class="bi bi-list fs-3"></i>
        </div>
      </div>
      <div class="offcanvas offcanvas-end"
           tabindex="-1"
           id="offcanvasNavbarLight"
           aria-labelledby="offcanvasNavbarLightLabel">
        <div class="offcanvas-header bg-sahibin-dark py-2">
          <a class="navbar-brand sahibin-logo fw-bold p-0 rounded-1" href="/">sahibin</a>
          <div role="button" data-bs-dismiss="offcanvas" aria-label="Close" class="text-white">
            <i class="bi bi-x fs-3"></i>
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


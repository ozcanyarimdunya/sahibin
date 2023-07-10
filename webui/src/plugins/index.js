import ace from 'ace-builds';
import {Popover, Tooltip} from "bootstrap";

import themeChromeUrl from 'ace-builds/src-noconflict/theme-chrome?url';

export const setupAceEditor = () => {
    ace.config.setModuleUrl('ace/theme/chrome', themeChromeUrl);
}

export const setupBootstrap = () => {
    document
        .querySelectorAll('[data-bs-toggle="popover"]')
        .forEach(popover => new Popover(popover, {trigger: 'focus'}));
    document
        .querySelectorAll('[data-bs-toggle="tooltip"]')
        .forEach(tooltip => new Tooltip(tooltip, {}));
}


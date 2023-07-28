import ace from 'ace-builds';
import {Popover, Tooltip} from "bootstrap";

import themeChromeUrl from 'ace-builds/src-noconflict/theme-chrome?url';
import 'ace-builds/src-noconflict/ext-searchbox'
import 'ace-builds/src-noconflict/ext-prompt'
import 'ace-builds/src-noconflict/ext-command_bar'

export const setupAceEditor = () => {
    ace.config.setModuleUrl('ace/theme/chrome', themeChromeUrl);
    ace.require('ace/ext/searchbox');
    ace.require('ace/ext/prompt');
    ace.require('ace/ext/command_bar');
}

export const setupBootstrap = () => {
    document
        .querySelectorAll('[data-bs-toggle="popover"]')
        .forEach(popover => new Popover(popover, {trigger: 'focus'}));
    document
        .querySelectorAll('[data-bs-toggle="tooltip"]')
        .forEach(tooltip => new Tooltip(tooltip, {}));
}


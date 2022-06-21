import socketClient from 'socket.io-client';
import { requestAuthListener, requestInfoListener, joinListener, commandListener, fileSaveListener, fileFetchListener, messageListener } from './listener';
import state from '../state';
import { print } from '../utility';

let socket: SocketIOClient.Socket|undefined;

export const startClient = (ip: string, port: number, key: string) => {

    socket = socketClient(`ws://${ip}:${port}`);

    state.isConnected = true;

    // listeners
    requestAuthListener(socket, key);
    requestInfoListener(socket);
    joinListener(socket);
    commandListener(socket);
    fileSaveListener(socket);
    fileFetchListener(socket);
    messageListener(socket);

};

export const endClient = () => {

    if(socket !== undefined) {

        socket.close();
        socket = undefined;

        print('network', `Socket client ended`);

    }

};

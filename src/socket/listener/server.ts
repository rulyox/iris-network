import { Socket } from 'socket.io';
import { authEvent, infoEvent, requestInfoEvent, messageEvent, joinEvent } from '../event';
import { parseAuth, parseInfo } from './parsers';
import state from '../../state';
import { print } from '../../utility';

export const authListener = (socket: Socket) => {

    socket.on(authEvent, (arg) => {

        const result = parseAuth(arg);

        if(result.result) {

            socket.emit(requestInfoEvent);

        } else {

            socket.emit(messageEvent, result.message);
            socket.disconnect();

        }

    });

};

export const infoListener = (socket: Socket) => {

    socket.on(infoEvent, (arg) => {

        const result = parseInfo(arg);

        if(result.result) {

            if(result.id !== null && result.name !== null && result.ip !== null && result.apiPort !== null && result.socketPort !== null) {

                const id: string = result.id;
                const name: string = result.name;
                const ip: string = result.ip;
                const apiPort: number = result.apiPort;
                const socketPort: number = result.socketPort;

                print('network', `${name} joined network`);

                state.addSocketClient(id, socket, name, ip, apiPort, socketPort);

                socket.emit(joinEvent, {
                    networkConfig: state.networkConfig,
                    networkMap: state.networkMap,
                    id: state.id
                });

            }

        } else {

            socket.emit(messageEvent, result.message);
            socket.disconnect();

        }

    });

};

export const disconnectListener = (socket: Socket) => {

    socket.on('disconnect', (reason) => {

        const socketId = socket.id;
        const id = state.getIdFromSocketId(socketId);
        const name = state.networkMap[id].name;

        print('network', `Socket ${socketId} disconnected : ${reason}`);

        print('network', `${name} left network`);

        state.removeSocketClient(socketId);

    });

};

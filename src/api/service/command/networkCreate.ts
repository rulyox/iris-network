import state from '../../../state';
import socket from '../../../socket';
import ServiceResult from '../ServiceResult';

const networkCreate = (options: any): ServiceResult => {

    if(state.isConnected) return new ServiceResult(false, 'Already connected to a network');

    if(options.config !== undefined) {

        const config = options.config;

        if(config.name !== undefined && config.mode !== undefined && config.key !== undefined) {

            const networkConfig = {
                name: config.name,
                mode: config.mode,
                key: config.key
            };

            socket.server.startServer();

            // set state
            state.isConnected = true;
            state.isGenesis = true;
            state.networkConfig = networkConfig;
            state.networkMap[state.id] = {
                name: state.name,
                ip: state.ip,
                apiPort: state.apiPort,
                socketPort: state.socketPort,
                role: 'master'
            };

            return new ServiceResult(true, null);

        } else {

            return new ServiceResult(false, 'Config has missing keys');

        }

    } else {

        return new ServiceResult(false, 'Wrong option');

    }

};

export default networkCreate;
